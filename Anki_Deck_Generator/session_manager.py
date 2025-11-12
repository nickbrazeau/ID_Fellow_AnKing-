#!/usr/bin/env python3
"""
Session Manager for Long-Running Anki Card Generation

Handles:
- Progress tracking across sessions
- Resumable card generation
- Conversation memory
- Graceful interruption handling
"""

import json
import os
from datetime import datetime
from pathlib import Path


class SessionManager:
    """Manages card generation progress and session state."""

    def __init__(self, base_dir="."):
        self.base_dir = Path(base_dir)
        self.progress_file = self.base_dir / "progress_tracker.json"
        self.session_log = self.base_dir / "session_log.jsonl"
        self.metadata_file = self.base_dir / "card_metadata.json"

        self.load_progress()

    def load_progress(self):
        """Load current progress from file."""
        if self.progress_file.exists():
            with open(self.progress_file, 'r') as f:
                self.progress = json.load(f)
        else:
            self.progress = self._create_default_progress()

    def save_progress(self):
        """Save current progress to file."""
        self.progress['last_updated'] = datetime.now().isoformat()[:10]
        with open(self.progress_file, 'w') as f:
            json.dump(self.progress, f, indent=2)

    def log_session(self, event_type, data):
        """Append event to session log."""
        event = {
            "timestamp": datetime.now().isoformat(),
            "type": event_type,
            "data": data
        }
        with open(self.session_log, 'a') as f:
            f.write(json.dumps(event) + '\n')

    def get_next_card_id(self):
        """Get next available card ID and increment."""
        next_id = self.progress['next_id']
        self.progress['next_id'] += 1
        self.save_progress()
        return next_id

    def mark_topic_started(self, category, topic):
        """Mark a topic as in progress."""
        if category in self.progress['topics']:
            self.progress['topics'][category]['status'] = 'in_progress'
            self.progress['current_topic'] = f"{category}/{topic}"
            self.save_progress()
            self.log_session('topic_started', {
                'category': category,
                'topic': topic
            })

    def mark_card_completed(self, category, card_id, card_file):
        """Mark a card as completed."""
        if category in self.progress['topics']:
            self.progress['topics'][category]['completed_cards'].append({
                'id': card_id,
                'file': card_file,
                'completed_at': datetime.now().isoformat()
            })
            # Increment total cards generated
            self.progress['total_cards_generated'] = self.progress.get('total_cards_generated', 0) + 1
            self.save_progress()
            self.log_session('card_completed', {
                'category': category,
                'card_id': card_id,
                'file': card_file
            })

    def mark_topic_completed(self, category, topic=None):
        """Mark a topic as completed. If no topic, marks entire category."""
        if topic:
            # Mark specific topic complete
            self.progress['completed_topics'] += 1
            self.progress['current_topic'] = None
            self.save_progress()
            self.log_session('topic_completed', {
                'category': category,
                'topic': topic
            })
        elif category in self.progress['topics']:
            # Mark entire category complete
            self.progress['topics'][category]['status'] = 'completed'
            self.progress['current_topic'] = None
            self.save_progress()
            self.log_session('category_completed', {'category': category})

    def get_resume_point(self):
        """Determine where to resume card generation."""
        current = self.progress.get('current_topic')
        if current:
            return current

        # Find first incomplete category
        for category, data in self.progress['topics'].items():
            if data['status'] != 'completed':
                return f"{category}/{data['subtopics'][0]}"

        return None

    def get_progress_summary(self):
        """Get human-readable progress summary."""
        total_topics = self.progress['total_topics']
        completed_topics = self.progress['completed_topics']
        total_cards = self.progress.get('total_cards_generated', 0)
        estimated_total = self.progress.get('estimated_total_cards', 1480)

        topic_percent = (completed_topics / total_topics * 100) if total_topics > 0 else 0
        card_percent = (total_cards / estimated_total * 100) if estimated_total > 0 else 0

        summary = {
            'total_topics': total_topics,
            'completed_topics': completed_topics,
            'remaining_topics': total_topics - completed_topics,
            'topic_percent_complete': f"{topic_percent:.1f}%",
            'total_cards_generated': total_cards,
            'estimated_total_cards': estimated_total,
            'card_percent_complete': f"{card_percent:.1f}%",
            'avg_cards_per_topic': round(total_cards / completed_topics, 1) if completed_topics > 0 else 0,
            'current_topic': self.progress.get('current_topic'),
            'next_id': self.progress['next_id']
        }

        # Category breakdown
        summary['by_category'] = {}
        for cat, data in self.progress['topics'].items():
            summary['by_category'][cat] = {
                'status': data['status'],
                'cards_completed': len(data['completed_cards'])
            }

        return summary

    def create_session_resume_file(self):
        """Create a markdown file for Claude to read on resume."""
        resume_file = self.base_dir / "SESSION_RESUME.md"
        summary = self.get_progress_summary()

        content = f"""# Session Resume - Anki Card Generation

## Last Session: {self.progress['last_updated']}

## Progress Summary
- **Total Cards Generated:** {summary['total_cards_generated']} (estimated total: ~{summary['estimated_total_cards']})
- **Card Progress:** {summary['card_percent_complete']}
- **Topics Completed:** {summary['completed_topics']} / {summary['total_topics']} ({summary['topic_percent_complete']})
- **Avg Cards/Topic:** {summary['avg_cards_per_topic']}
- **Next Card ID:** {summary['next_id']}
- **Current Topic:** {summary['current_topic'] or 'Not set'}

## Category Status

"""

        for cat, data in summary['by_category'].items():
            status_emoji = "✅" if data['status'] == 'completed' else "🔄" if data['status'] == 'in_progress' else "⏳"
            content += f"{status_emoji} **{cat}**: {data['status']} ({data['cards_completed']} cards)\n"

        content += f"""

## Recent Activity

"""

        # Read last 10 session log entries
        if self.session_log.exists():
            with open(self.session_log, 'r') as f:
                lines = f.readlines()
                recent = lines[-10:] if len(lines) > 10 else lines

                for line in recent:
                    event = json.loads(line)
                    ts = event['timestamp'][:19]  # Just datetime, no microseconds
                    content += f"- `{ts}` {event['type']}: {json.dumps(event['data'])}\n"

        content += f"""

## Instructions for Claude

1. **Read this file** at start of each session
2. **Check progress_tracker.json** for detailed status
3. **Resume from:** `{summary['current_topic'] or 'First incomplete topic'}`
4. **Use `session_manager.py`** to log progress
5. **Update after each card** with `mark_card_completed()`

## Quick Commands

```python
from session_manager import SessionManager
sm = SessionManager()

# Get resume point
resume_point = sm.get_resume_point()

# Start new topic
sm.mark_topic_started('category', 'topic')

# Get next card ID
card_id = sm.get_next_card_id()

# Mark card done
sm.mark_card_completed('category', card_id, 'filename.md')

# Check progress
summary = sm.get_progress_summary()
```
"""

        with open(resume_file, 'w') as f:
            f.write(content)

        return str(resume_file)

    def _create_default_progress(self):
        """Create default progress structure."""
        return {
            "version": "1.0",
            "last_updated": datetime.now().isoformat()[:10],
            "total_topics": 296,
            "completed_topics": 0,
            "current_topic": None,
            "next_id": 10,
            "topics": {},
            "session_history": [],
            "notes": ""
        }


def main():
    """Test and demonstrate session manager."""
    sm = SessionManager()

    print("=== Session Manager Status ===")
    summary = sm.get_progress_summary()
    print(f"Cards Generated: {summary['total_cards_generated']}/{summary['estimated_total_cards']} ({summary['card_percent_complete']})")
    print(f"Topics Completed: {summary['completed_topics']}/{summary['total_topics']} ({summary['topic_percent_complete']})")
    print(f"Avg Cards/Topic: {summary['avg_cards_per_topic']}")
    print(f"Current: {summary['current_topic']}")
    print(f"Next ID: {summary['next_id']}")

    print("\n=== Creating Resume File ===")
    resume_file = sm.create_session_resume_file()
    print(f"Created: {resume_file}")

    print("\n=== Resume Point ===")
    resume_point = sm.get_resume_point()
    print(f"Resume from: {resume_point}")


if __name__ == "__main__":
    main()
