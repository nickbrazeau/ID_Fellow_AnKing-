#!/usr/bin/env python3
"""
Convert markdown flashcards to TSV format for Anki import.

Usage:
    python convert_to_anki.py [--output OUTPUT_FILE]

The script scans the cards/ directory for .md files, parses them,
and generates a TSV file compatible with Anki import.
"""

import os
import re
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

try:
    import yaml
except ImportError:
    yaml = None


class AnkiCardConverter:
    """Converts markdown flashcards to Anki TSV format."""

    def __init__(self, cards_dir: str = "cards", images_dir: str = "images"):
        self.cards_dir = Path(cards_dir)
        self.images_dir = Path(images_dir)
        self.metadata = {"cards": [], "last_id": 0}
        self.metadata_file = Path("card_metadata.json")
        self.load_metadata()

    def load_metadata(self):
        """Load existing card metadata if available."""
        if self.metadata_file.exists():
            with open(self.metadata_file, 'r') as f:
                self.metadata = json.load(f)

    def save_metadata(self):
        """Save card metadata to JSON file."""
        with open(self.metadata_file, 'w') as f:
            json.dump(self.metadata, f, indent=2)

    def parse_frontmatter(self, content: str) -> tuple:
        """Extract YAML frontmatter and remaining content."""
        frontmatter = {}
        body = content

        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                if yaml:
                    try:
                        frontmatter = yaml.safe_load(parts[1]) or {}
                        body = parts[2].strip()
                    except yaml.YAMLError:
                        pass
                else:
                    # Fallback: parse manually if yaml not available
                    for line in parts[1].strip().split('\n'):
                        if ':' in line:
                            key, value = line.split(':', 1)
                            key = key.strip()
                            value = value.strip()
                            # Handle list values like tags: [a, b, c]
                            if value.startswith('[') and value.endswith(']'):
                                value = [v.strip() for v in value[1:-1].split(',')]
                            frontmatter[key] = value
                    body = parts[2].strip()

        return frontmatter, body

    def extract_card_content(self, body: str) -> Dict[str, str]:
        """Extract Q, A, Media, and Sources from markdown body."""
        card = {
            "question": "",
            "answer": "",
            "media": "",
            "sources": ""
        }

        # Try format 1: ## Question / ## Answer (header format)
        q_match = re.search(r'##\s*Question\s*\n+(.+?)(?=##\s*Answer)', body, re.DOTALL)
        if q_match:
            card["question"] = q_match.group(1).strip()

        # Try format 2: **Q:** / **A:** (bold format) if header format not found
        if not card["question"]:
            q_match = re.search(r'\*\*Q:\*\*\s*(.+?)(?=\*\*A:\*\*)', body, re.DOTALL)
            if q_match:
                card["question"] = q_match.group(1).strip()

        # Extract answer - try header format first
        a_match = re.search(r'##\s*Answer\s*\n+(.+?)(?=##\s*(?:Key Points|Sources|Media)|\*\*(?:Key Points|Media|Sources):\*\*|$)', body, re.DOTALL)
        if a_match:
            card["answer"] = a_match.group(1).strip()
        else:
            # Try bold format
            a_match = re.search(r'\*\*A:\*\*\s*(.+?)(?=\*\*(?:Key Points|Media|Sources):\*\*|$)', body, re.DOTALL)
            if a_match:
                card["answer"] = a_match.group(1).strip()

        # Extract Key Points if present (header format)
        kp_match = re.search(r'##\s*Key Points\s*\n+(.+?)(?=##\s*(?:Sources|Media)|\*\*(?:Media|Sources):\*\*|$)', body, re.DOTALL)
        if kp_match:
            card["answer"] += "\n\n### Key Points\n\n" + kp_match.group(1).strip()
        else:
            # Try bold format for Key Points
            kp_match = re.search(r'\*\*Key Points:\*\*\s*(.+?)(?=\*\*(?:Media|Sources):\*\*|$)', body, re.DOTALL)
            if kp_match:
                card["answer"] += "\n\n### Key Points\n\n" + kp_match.group(1).strip()

        # Extract media (try header format first)
        m_match = re.search(r'##\s*Media\s*\n+(.+?)(?=##\s*Sources|\*\*Sources:\*\*|$)', body, re.DOTALL)
        if m_match:
            card["media"] = m_match.group(1).strip()
        else:
            # Try bold format
            m_match = re.search(r'\*\*Media:\*\*\s*(.+?)(?=\*\*Sources:\*\*|$)', body, re.DOTALL)
            if m_match:
                card["media"] = m_match.group(1).strip()

        # Extract sources (try header format first)
        s_match = re.search(r'##\s*Sources\s*\n+(.+?)(?=##\s*Media|\*\*Media:\*\*|$)', body, re.DOTALL)
        if s_match:
            card["sources"] = s_match.group(1).strip()
        else:
            # Try bold format
            s_match = re.search(r'\*\*Sources:\*\*\s*(.+?)(?=\*\*Media:\*\*|$)', body, re.DOTALL)
            if s_match:
                card["sources"] = s_match.group(1).strip()

        return card

    def markdown_to_html(self, text: str) -> str:
        """Convert markdown formatting to HTML."""
        # Bold: **text** or __text__ -> <b>text</b>
        text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
        text = re.sub(r'__(.+?)__', r'<b>\1</b>', text)

        # Italic: *text* or _text_ -> <i>text</i>
        text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
        text = re.sub(r'_(.+?)_', r'<i>\1</i>', text)

        # Code: `text` -> <code>text</code>
        text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)

        return text

    def format_for_anki(self, card_data: Dict, frontmatter: Dict) -> List[str]:
        """Format card data as TSV row for Anki."""
        # Get deck name (default to "Infectious Diseases")
        deck = frontmatter.get("deck", "Infectious Diseases")

        # Build the front of the card (question) - convert markdown to HTML
        front = self.markdown_to_html(card_data["question"])

        # Build the back of the card (answer + optional media) - convert markdown to HTML
        back = self.markdown_to_html(card_data["answer"])
        if card_data["media"] and card_data["media"].strip():
            media = card_data["media"].strip()
            # Only add images if we have actual image files (not just references)
            # Check for markdown image syntax: ![alt](path/to/image.ext)
            img_match = re.search(r'!\[.*?\]\((.+?\.(jpg|jpeg|png|gif|svg))\)', media, re.IGNORECASE)
            if img_match:
                img_path = img_match.group(1)
                # Check if the image file actually exists
                image_file = self.images_dir / Path(img_path).name
                if image_file.exists() and image_file.stat().st_size > 1000:  # > 1KB (not a redirect)
                    img_filename = image_file.name
                    back += f'<br><br><img src="{img_filename}">'
            # If media is just a reference (e.g., "See Figure X in PMC..."), skip it
            # We don't want broken image tags

        # Extra field (sources)
        extra = card_data["sources"]

        # Tags
        tags_list = frontmatter.get("tags", [])
        if isinstance(tags_list, list):
            tags = " ".join(tags_list)
        else:
            tags = str(tags_list)

        # Return as TSV row (deck, front, back, extra, tags)
        return [deck, front, back, extra, tags]

    def process_card_file(self, filepath: Path) -> Optional[List[str]]:
        """Process a single markdown card file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            frontmatter, body = self.parse_frontmatter(content)
            card_data = self.extract_card_content(body)

            if not card_data["question"] or not card_data["answer"]:
                print(f"Warning: Skipping {filepath.name} - missing question or answer")
                return None

            # Update metadata
            card_id = frontmatter.get("id", filepath.stem)
            card_meta = {
                "id": card_id,
                "file": str(filepath.relative_to(self.cards_dir.parent)),
                "modified": frontmatter.get("modified", datetime.now().isoformat()[:10])
            }

            # Update or add to metadata
            existing = next((c for c in self.metadata["cards"] if c["id"] == card_id), None)
            if existing:
                existing.update(card_meta)
            else:
                self.metadata["cards"].append(card_meta)

            return self.format_for_anki(card_data, frontmatter)

        except Exception as e:
            print(f"Error processing {filepath.name}: {e}")
            return None

    def convert_all_cards(self, output_file: str = None) -> str:
        """Convert all markdown cards to TSV format."""
        if output_file is None:
            timestamp = datetime.now().strftime("%Y-%m-%d")
            output_file = f"generated_decks/ID_deck_{timestamp}.tsv"

        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Find all markdown files recursively in cards/
        card_files = sorted(self.cards_dir.rglob("*.md"))

        if not card_files:
            print(f"No markdown files found in {self.cards_dir}")
            return ""

        print(f"Found {len(card_files)} card files")

        # Process all cards
        rows = []
        for card_file in card_files:
            row = self.process_card_file(card_file)
            if row:
                rows.append(row)

        # Write TSV file (no header, no Deck column - just Front, Back, Tags)
        with open(output_path, 'w', encoding='utf-8') as f:
            # Write all rows (skip Deck column which is row[0])
            for row in rows:
                # Skip the Deck column (row[0]), keep Front (row[1]), Back (row[2]), Tags (row[4])
                # Skip Extra (row[3]) as it's not used
                anki_row = [row[1], row[2], row[4]]  # Front, Back, Tags
                # Escape tabs and newlines in content
                escaped_row = [field.replace('\t', ' ').replace('\n', '<br>') for field in anki_row]
                f.write('\t'.join(escaped_row) + '\n')

        # Save metadata
        self.save_metadata()

        print(f"\nSuccessfully converted {len(rows)} cards")
        print(f"Output written to: {output_path}")
        print(f"Metadata saved to: {self.metadata_file}")

        return str(output_path)


def main():
    parser = argparse.ArgumentParser(
        description="Convert markdown flashcards to Anki TSV format"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output TSV file path (default: generated_decks/ID_deck_YYYY-MM-DD.tsv)"
    )
    parser.add_argument(
        "--cards-dir", "-c",
        default="cards",
        help="Directory containing markdown card files (default: cards)"
    )

    args = parser.parse_args()

    converter = AnkiCardConverter(cards_dir=args.cards_dir)
    converter.convert_all_cards(output_file=args.output)


if __name__ == "__main__":
    main()
