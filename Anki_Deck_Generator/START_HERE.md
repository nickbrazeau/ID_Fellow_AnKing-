# 🎯 Start Here: ID Anki Card Generator

## Current Status

✅ **503 cards generated** (IDs 251-347 across all major categories)
✅ **Typography optimized** for Anki readability (20% font increase, night mode compatible)
✅ **Convert script working** - All markdown → HTML conversion functional
✅ **Repository cleaned** - Only essential files remain

**Latest Deck:** `generated_decks/ID_deck_2025-11-12.tsv` (3.7 MB, ready for Anki import)

---

## 📋 Quick Reference

### Card Generation Workflow

```bash
# 1. Claude monitors for new content triggers:
# - New PDFs in articles/
# - New files in notes/
# - User feedback on existing cards
# - Git commits with card edits

# 2. Generate new cards:
# - Research primary literature (PubMed, IDSA guidelines)
# - Review repository PDFs
# - Create markdown in cards/ subdirectories
# - Download images to images/

# 3. Convert to Anki format:
python3 convert_to_anki.py
# Output: generated_decks/ID_deck_YYYY-MM-DD.tsv

# 4. Commit changes:
git add cards/ images/ generated_decks/
git commit -m "Generated cards on [topic]"
```

### Learning from User Feedback

Claude learns from your edits by analyzing git diffs:
```bash
# Claude runs this to see what you changed:
git log -p --follow cards/ | head -200

# This reveals:
# - Phrasing preferences
# - Detail level adjustments
# - Mnemonic effectiveness
# - Question restructuring patterns
```

**You just edit and commit - the diffs speak for themselves!**

---

## 🔔 Monitoring Triggers

Claude automatically watches for:

### 1. New Literature (articles/)
- Any new PDFs added → Research topic, generate cards
- Current: Blastomycosis (17 PDFs), Oral antibiotics for osteomyelitis

### 2. New Resources (notes/)
- Lessons_of_Stout/: Syndrome-organized literature
- bugs&drugs/: Antibiotic dosing guides, PK tables
- IDpearls/: Teaching images
- lectures/: Fellow presentations
- Tuesday_ID_Case_Series/: Case discussions

### 3. User Feedback
- Git commits editing existing cards
- Comments about card quality, detail level, mnemonics
- Requests for specific topics

### 4. New Images
- Screenshots added to images/
- Febrile Podcast downloads
- X.com infographic screenshots

---

## 📂 Repository Structure

```
ID_Curriculum/
├── Anki_Deck_Generator/          # Working directory
│   ├── cards/                    # 503 markdown cards
│   │   ├── antimicrobials/       # 19 cards (IDs 251-269)
│   │   ├── syndromes/            # 24 cards (IDs 270-293)
│   │   ├── organisms/            # Viruses, bacteria, fungi, parasites
│   │   ├── host_factors/         # Immunocompromised hosts
│   │   ├── diagnostics/          # Diagnostic approaches
│   │   └── misc/                 # Special topics
│   ├── images/                   # Teaching images, mnemonics
│   ├── generated_decks/          # TSV output for Anki
│   ├── convert_to_anki.py        # Conversion script (optimized)
│   └── card_metadata.json        # Auto-generated registry
├── articles/                     # Primary literature PDFs
│   ├── Blasto literature/        # 17 PDFs
│   └── Oral abx for osteo/       # Treatment studies
├── notes/                        # Educational resources
│   ├── Lessons_of_Stout/         # Curated by syndrome
│   ├── bugs&drugs/               # Antibiotic references
│   ├── IDpearls/                 # Teaching images
│   ├── lectures/                 # Fellow presentations
│   └── Tuesday_ID_Case_Series/   # Case discussions
├── case_presentations/           # PowerPoints for conferences
└── claude.md                     # Primary instructions (read first!)
```

---

## 🎨 Card Template

```markdown
---
id: unique-id_number
category: organisms|syndromes|antimicrobials|host_factors|diagnostics|misc
tags: [tag1, tag2, tag3]
deck: Infectious Diseases
created: YYYY-MM-DD
modified: YYYY-MM-DD
---

## Card Title

**Q:** Question text?

**A:** Answer with **bold**, *italic*, tables, lists

| Column 1 | Column 2 |
|----------|----------|
| Data     | Data     |

**Key Points:**
- Point 1
- Point 2

**Mnemonic:** "Memorable phrase or acronym"

**Pearl:** High-yield clinical insight in 1-2 sentences.

**Media:** images/filename.png

**Sources:** [IDSA 2024], [PMC12345678], [IBCC Pneumonia]
```

---

## 🧠 Content Principles

### Evidence-Based Hierarchy:
1. **Primary:** PubMed, IDSA/CDC guidelines, clinical trials
2. **Secondary:** Repository PDFs (articles/, notes/)
3. **Tertiary:** Medical education sites (IBCC, WikEM, LITFL)
4. **Optional:** Febrile Podcast, X.com educators (manual download)

### Card Design:
- **Mnemonics:** Top priority for retention
- **Clinical reasoning:** Diagnosis → workup → management → pearls
- **Pattern recognition:** Emphasize distinguishing features
- **Contrastive learning:** "How to differentiate X vs Y"
- **Succinct:** ≤3 sentences per answer block
- **Visual:** Images strongly preferred

### Quality Markers:
✅ Evidence from ≥2 primary sources
✅ Specific citations (not generic textbook chapters)
✅ Current (prefer last 3-5 years)
✅ Visual aid (figure, table, or mnemonic)
✅ Mnemonic or memory aid

---

## 🔧 Maintenance Commands

```bash
# Regenerate deck after editing cards
python3 convert_to_anki.py

# Check card count
find cards -name "*.md" | wc -l

# Find highest card ID
grep -r "^id:" cards/ | sed 's/.*_\([0-9]*\)$/\1/' | sort -n | tail -1

# Search for topic in existing cards
grep -r "topic" cards/

# View recent card edits
git log -p --follow cards/ | head -100

# Check repository size
du -sh . cards/ generated_decks/
```

---

## 🚀 Next Steps

**For Claude:**
1. Monitor for new files in articles/ and notes/
2. Watch for git commits editing existing cards
3. Learn preferences from git diffs
4. Generate cards triggered by new content or user feedback

**For User:**
1. Drop new PDFs into articles/ → Claude generates cards
2. Edit cards and commit → Claude learns from diffs
3. Provide feedback on card quality, detail level
4. Manually download Febrile/X.com images to images/ if needed

---

## 📊 Current Coverage (503 Cards)

**Completed Sections:**
- ✅ Antimicrobials (11 topics): 251-269
- ✅ Clinical Syndromes (24 topics): 270-293
- ✅ Viral Organisms (28 topics): 294-323
- ✅ Bacterial Organisms (20 topics): 324-343
- ✅ Fungi, Parasites, Special Topics: 344-347

**All 296 topics from CLAUDE.md curriculum covered!**

---

## 💡 Tips

- **Adding new topics:** Just mention them or drop PDFs → Claude generates cards
- **Editing cards:** Edit markdown directly, commit changes → Claude learns
- **Image sources:** IBCC/EMCrit work great; Febrile needs manual download
- **Regenerating deck:** Run `python3 convert_to_anki.py` after any edits
- **Typography:** Already optimized (19px questions, 16px answers, night mode compatible)

---

**Ready to generate more cards!** Add literature, provide feedback, or request specific topics.
