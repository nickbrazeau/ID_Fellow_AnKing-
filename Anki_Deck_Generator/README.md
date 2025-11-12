# Anki Deck Generator for Infectious Diseases

This directory contains a complete system for generating Anki flashcards with:
- 📝 Human-readable markdown format
- 🔄 Git version control for learning from edits
- 💾 Progress persistence across sessions
- 🧠 Conversation memory for Claude continuity
- 🚫 Interruption-proof (survives shutdowns)

---

## 🚀 For Claude: Start Every Session Here

**Read in this order:**
1. **`START_HERE.md`** - Complete startup checklist
2. **`CONVERSATION_CONTEXT.md`** - Full conversation history
3. **`SESSION_RESUME.md`** - Current progress

These files ensure full context even after terminal/session loss.

---

## Quick Start (For Users)

### 1. Generate Cards
Create markdown files in the `cards/` subdirectories using the template format.

### 2. Convert to Anki Format
```bash
python3 convert_to_anki.py
```

This generates a TSV file in `generated_decks/` ready for Anki import.

### 3. Import to Anki
In Anki: **File > Import** → Select the generated TSV file

## Directory Structure

```
├── cards/                  # Markdown card files organized by category
│   ├── antimicrobials/
│   ├── syndromes/
│   ├── organisms/
│   ├── host_factors/
│   ├── diagnostics/
│   └── misc/
├── images/                 # Images, mnemonics, schematics
├── generated_decks/        # TSV output files (git-ignored)
├── prior_decks/            # Legacy CSV deck (~230 cards)
└── convert_to_anki.py      # Conversion script
```

## Card Template

Create files as: `<category>_<topic>_<id>.md`

```markdown
---
id: endocarditis_culture-negative_001
category: syndromes
tags: [endocarditis, diagnosis, culture-negative]
deck: Infectious Diseases
created: 2025-01-08
modified: 2025-01-08
---

## Culture-Negative Endocarditis

**Q:** What are the major causes of culture-negative endocarditis?

**A:** *Answer text here with **bold** for emphasis.*

**Media:** images/mnemonic.png

**Sources:** [IBCC], [Febrile Podcast]
```

## Conversion Script

**Usage:**
```bash
python3 convert_to_anki.py [--output FILENAME]
```

**Features:**
- Recursively scans `cards/` for `.md` files
- Parses YAML frontmatter
- Converts images to Anki HTML format
- Generates card metadata registry
- No external dependencies required (works without PyYAML)

## Git Workflow

```bash
# After generating cards
git add cards/ images/
git commit -m "Generated cards on [topic]"

# After editing cards
git add cards/
git commit -m "Reviewed batch 1"
```

Claude can analyze git diffs to learn from your edits and improve future card generation.

## Requirements

- Python 3.x (standard library only)
- Optional: PyYAML for better frontmatter parsing
