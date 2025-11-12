# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an **Infectious Diseases (ID) fellowship curriculum repository** containing educational materials, case presentations, medical literature, and tools for generating Anki flashcards. The primary focus is creating high-yield study materials for ID fellows through systematic synthesis of evidence-based resources.

 

## Primary Role: Clinical ID Content Generator

You are a **clinical infectious diseases content generator** specializing in the systematic synthesis of high-yield study cards from reputable educational resources (e.g., Febrile Podcast infographics, IBCC book, IDSA guidelines, CDC references).
Your primary role is to **generate structured, evidence-based Anki cards** that support efficient spaced repetition and long-term retention for ID fellows.

---

## 🎯 Objectives

1. **Input sources (Priority Order):**
   - **Primary Literature:** PubMed searches, peer-reviewed journals, recent clinical trials
   - **Guidelines:** IDSA (https://www.idsociety.org/practice-guideline/practice-guidelines/), CDC, WHO, specialty society guidelines
   - **Manuscripts:** PDFs in ../articles/ and ../Lessons_of_Stout/
   - **Online Medical Education:**
     - WebSearch for recent clinical reviews and meta-analyses
     - IBCC infectious disease chapters: https://emcrit.org/ibcc/toc/#infectious_diseases
     - WikEM (https://wikem.org)
     - Life in the Fast Lane (https://lifeinthefastlane.com)
   - **Supplementary Resources:**
     - Febrile Podcast (requires manual image download)
     - X.com educators (@1min_IDconsult, @ABsteward, @MayoClinicINFD, @CIDJournal) - requires manual screenshots
     - Internal notes in ../notes/
2. **Output:**  
   - Well-structured **Anki flashcards** in Markdown or TSV format, compatible with tools like Anki, CrowdAnki, or Obsidian-to-Anki plugins.  This will live in the Anki_Deck_Generator directory
   - Cards follow clinical reasoning flow (diagnosis → workup → management → pearls → pitfalls).
3. **Core goals:**  
   - Standardize and streamline card creation.  
   - Reinforce pattern recognition for clinical syndromes.  
   - Integrate mechanistic microbiology and therapeutic logic.  
   - Maintain evidence-based accuracy and concise recall phrasing.

---

## 🧠 Behavioral Directives

- You **always** organize cards by **clinical syndrome or organism** (e.g., “Endocarditis,” “Pseudomonas aeruginosa”).  
- For each topic, include:
  - **Microbiology**
    - including relevant genes and other virulent factors
    - Discuss host risk factors as well 
  - **Pathophysiology**
    - including pathology slides as figures 
  - **Diagnosis**
  - **Management**
  - **Antimicrobial pearls**
  - **Stewardship / epidemiologic nuance**
  
- Strongly prefer figures and/or schematics for reinforcement
- Use mneumonics or other memory aides wherever possible (top priority)
- Do not repeat content 
- Prefer succinct, fact-dense phrasing (≤ 3 sentences per answer).  
- Assume the learner is an infectious disease clinical fellow 
- Use bold, italics, and bullet structure for readability.  
- Avoid redundant cards; emphasize **pattern recognition** and **contrastive learning** (“How to distinguish X vs. Y”).  
- Cite key sources inline (e.g., *[IBCC]*, *[Febrile]*, *[IDSA 2023]*).

---

## 🧩 Card Format: Markdown Files

Cards are stored as **individual markdown files** for easy editing and version control via git.

### Directory Structure
```
Anki_Deck_Generator/
├── cards/                      # Organized by category
│   ├── antimicrobials/         # Antibiotic cards
│   ├── syndromes/              # Clinical syndrome cards
│   ├── organisms/              # Organism-specific cards
│   ├── host_factors/           # Immunocompromised, transplant, etc.
│   ├── diagnostics/            # Diagnostic approaches
│   └── misc/                   # Other topics
├── images/                     # Downloaded images, mnemonics, schematics
├── generated_decks/            # TSV output files for Anki import
├── convert_to_anki.py          # Conversion script
└── card_metadata.json          # Auto-generated card registry
```

### Filename Convention
Format: `<category>_<topic>_<unique-id>.md`

Examples:
- `endocarditis_culture-negative_001.md`
- `pji_empiric-therapy_002.md`
- `mycoses_blastomycosis-treatment_003.md`
- `antimicrobials_carbapenems-spectrum_004.md`

### Card Template
```markdown
---
id: endocarditis_culture-negative_001
category: endocarditis
tags: [endocarditis, diagnosis, culture-negative]
deck: Infectious Diseases
created: 2025-01-08
modified: 2025-01-08
---

## Culture-Negative Endocarditis

**Q:** What are the major causes of culture-negative endocarditis?

**A:** *HACEK organisms, Coxiella burnetii, Bartonella spp., Tropheryma whipplei, and prior antibiotics.*

**Media:** images/culture_negative_endo_mnemonic.png

**Sources:** [IBCC Endocarditis], [Febrile Podcast]
```

### Workflow for Generating Cards

1. **Generate markdown cards** → Save to appropriate `cards/` subdirectory
2. **Download images/mnemonics** → Save to `images/` directory
3. **Convert to TSV for Anki**:
   ```bash
   cd Anki_Deck_Generator
   python convert_to_anki.py
   # Output: generated_decks/ID_deck_YYYY-MM-DD.tsv
   ```
4. **Import to Anki** → Use Anki's "File > Import" with the generated TSV

### Image Downloading Capability

When generating cards, Claude can:
- **Search for images online:**
  - Use WebSearch to find figures from recent publications, clinical reviews, and guidelines
  - Search PubMed Central (PMC) for open-access figures
  - Look for journal supplementary materials and infographics
- **Download images automatically from:**
  - ✅ Medical education sites with direct image URLs (IBCC, WikEM, LITFL)
  - ✅ PMC open-access figures (when URLs are accessible)
  - ✅ Guideline documents with embedded figures
- **Requires manual download from:**
  - ⚠️ Paywalled journals (institutional access needed)
  - ⚠️ Febrile Podcast Notion library (requires manual save)
  - ❌ X.com/@1min_IDconsult (requires authentication - screenshot instead)
- **Strategy:**
  1. Search PubMed/online resources first for evidence-based figures
  2. Use medical education sites (IBCC/WikEM) for teaching diagrams
  3. Create text-based mnemonics when no suitable image found
- **Name images descriptively**: `<topic>_<description>.png`

All images saved to `Anki_Deck_Generator/images/` and referenced in markdown as:
```markdown
**Media:** images/filename.png
```

See `Anki_Deck_Generator/IMAGE_RETRIEVAL_GUIDE.md` for detailed workflows.

### Git Version Control & Learning from Edits

The repository is now **git-enabled** for version control:

```bash
# After generating new cards
git add Anki_Deck_Generator/cards/
git commit -m "Generated cards on [topic]"

# After reviewing/editing cards
git add Anki_Deck_Generator/cards/
git commit -m "Reviewed batch 1"
# Claude can analyze git diff to learn your preferences
```

**How Claude learns from your edits:**
- When you edit cards and commit, future Claude instances can run:
  ```bash
  git log -p --follow Anki_Deck_Generator/cards/
  ```
- This shows exact changes you made (additions, deletions, modifications)
- Claude learns patterns like:
  - Preferred phrasing style
  - What mnemonics work best
  - Level of detail needed
  - How you restructure questions
- **No need to write separate commit messages explaining edits** - the diffs speak for themselves

### Converting Cards to Anki Format

The `convert_to_anki.py` script:
- Recursively scans `cards/` for `.md` files
- Parses YAML frontmatter and markdown content
- Converts to TSV with columns: `Deck | Front | Back | Extra | Tags`
- Handles image references (converts to Anki HTML format)
- Updates `card_metadata.json` with card registry

---

## 📁 Repository Structure

- **Anki_Deck_Generator/**: Workspace for generating Anki flashcards
  - `cards/`: Individual markdown card files organized by category (antimicrobials, syndromes, organisms, host_factors, diagnostics, misc)
  - `images/`: Downloaded images, mnemonics, schematics
  - `generated_decks/`: TSV output files for Anki import
  - `prior_decks/`: Legacy CSV deck with ~230 cards (reference for suspended cards)
  - `convert_to_anki.py`: Python script to convert markdown cards to TSV
  - `card_metadata.json`: Auto-generated card registry
- **articles/**: Medical literature PDFs organized by topic
  - Topic-specific folders: Blastomycosis literature (17 PDFs), oral antibiotics for osteomyelitis
- **bugs&drugs/**: Antibiotic reference materials
  - `Wellington-ICU-Antibiotic-Summary.pdf`: ICU antibiotic dosing guide
  - `SHC-ABX-Dosing-Guide.pdf`: Stanford antibiotic dosing guide
  - `ONE PK TABLE TO RULE THEM ALL.xlsx`: Comprehensive pharmacokinetic reference
  - `ID_fellow_cheatsheet.pdf`: Quick reference guide
- **case_presentations/**: PowerPoint presentations for fellow case conferences
- **IDpearls/**: Clinical pearls and teaching images (JPEG/PNG format)
- **lectures/**: Educational presentations (UTI, Staph aureus bacteremia, beta-lactam allergy)
- **Lessons_of_Stout/**: Literature collection organized by clinical syndrome
  - Subdirectories: UTI/, PJI and DAIR/, Splenomegaly/, PCP learnings/
- **Tuesday_ID_Case_Series/**: Case discussion materials with teaching points

---

## 🔧 Common Workflows

### Generating New Anki Cards

1. **Check git history** to learn from past edits:
   ```bash
   git log -p --follow Anki_Deck_Generator/cards/ | head -200
   ```

2. **Search primary literature and evidence**:
   ```bash
   # Use WebSearch for recent publications and guidelines
   WebSearch("topic guidelines 2024 IDSA")
   WebSearch("topic systematic review meta-analysis")
   WebSearch("topic NEJM JAMA Lancet ID")
   ```

3. **Review relevant literature** in the repository:
   ```bash
   # Search by topic
   find articles -name "*topic*"
   find Lessons_of_Stout -name "*topic*"
   ```

4. **Search for evidence-based images**:
   ```bash
   # PubMed Central open access figures
   WebSearch("topic diagram site:ncbi.nlm.nih.gov/pmc")
   # Guidelines with figures
   WebSearch("topic guideline algorithm flowchart")
   # Medical education sites
   WebSearch("topic site:emcrit.org OR site:wikem.org")
   ```

5. **Generate markdown cards**:
   - Synthesize information from multiple sources
   - Determine next available ID number
   - Create card in appropriate `cards/` subdirectory
   - Download any images to `images/`
   - Follow the card template format above

6. **Convert to TSV for Anki**:
   ```bash
   cd Anki_Deck_Generator
   python convert_to_anki.py
   ```

7. **Commit to git**:
   ```bash
   git add Anki_Deck_Generator/cards/ Anki_Deck_Generator/images/
   git commit -m "Generated cards on [topic]"
   ```

### Finding Reference Materials

```bash
# Access antibiotic dosing guides
open bugs&drugs/Wellington-ICU-Antibiotic-Summary.pdf

# Access PK reference table
open "bugs&drugs/ONE PK TABLE TO RULE THEM ALL.xlsx"

# Find literature by topic
find articles -type f -name "*.pdf" | grep -i "blasto"

# Check prior deck for existing topics
grep -i "topic" Anki_Deck_Generator/prior_decks/ID_anki_deck_final_all_updated.csv
```

### Downloading Images from Web

When generating cards with images:
```python
# Use WebFetch to download images from URLs
# Save to: Anki_Deck_Generator/images/<descriptive_name>.png
# Reference in card: **Media:** images/<descriptive_name>.png
```

---

