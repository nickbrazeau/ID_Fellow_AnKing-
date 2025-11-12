# Infectious Diseases Fellowship Curriculum

## Overview

An evidence-based Anki flashcard generation system for infectious diseases education, built collaboratively between an ID fellow and Claude Code. This repository contains **503 high-yield Anki cards** covering the complete ID curriculum, optimized for spaced repetition learning.

---

## 🎯 Objectives

**Primary Goal:** Create comprehensive, evidence-based Anki flashcards that support ID fellowship training through:
- Systematic coverage of all major ID topics (antimicrobials, syndromes, organisms, host factors)
- Integration of primary literature, guidelines, and clinical reasoning
- Mnemonic-driven recall and pattern recognition
- Efficient spaced repetition for long-term retention

**Key Principles:**
- Evidence from peer-reviewed sources (PubMed, IDSA/CDC guidelines)
- Clinical reasoning flow (diagnosis → workup → management → pearls)
- Visual learning (figures, tables, mnemonics)
- Succinct, fellow-level content

---

## 📊 Current Status

### Completed Work (by Claude Code)

**503 Cards Generated** spanning all major ID topics:
- **Antimicrobials** (19 cards): β-lactams, carbapenems, novel therapies, antivirals, antiparasitics
- **Clinical Syndromes** (24 cards): Pneumonia, endocarditis, meningitis, osteomyelitis, UTI, sepsis
- **Viral Organisms** (28 cards): HIV, COVID-19, herpesviruses, respiratory viruses, hepatitis
- **Bacterial Organisms** (20+ cards): Staph, Strep, gram-negatives, anaerobes, atypicals
- **Fungi** (10+ cards): Endemic mycoses, Candida, Aspergillus, Cryptococcus, Pneumocystis
- **Parasites** (8+ cards): Malaria, toxoplasmosis, amebiasis, helminths
- **Special Topics**: Kawasaki disease, infection prevention, immunocompromised hosts

**Technical Achievements:**
- Markdown → HTML conversion with optimized typography (19px questions, 16px answers)
- Night mode compatible (dark blue table headers, proper contrast)
- Automatic image handling and table rendering
- Git version control for continuous learning from user edits
- Efficient TSV export for direct Anki import

---

## 🏗️ Repository Structure

```
ID_Curriculum/
├── Anki_Deck_Generator/          # Working directory (Claude's workspace)
│   ├── cards/                    # 503 markdown cards (organized by category)
│   ├── images/                   # Teaching images and mnemonics
│   ├── generated_decks/          # Ready-to-import TSV files
│   ├── convert_to_anki.py        # Conversion script (optimized by Claude)
│   └── START_HERE.md             # Workflow documentation
├── articles/                     # 63 PDFs: primary literature
├── notes/                        # Curated educational resources
│   ├── Lessons_of_Stout/         # 28 PDFs organized by syndrome
│   ├── bugs&drugs/               # Antibiotic dosing references
│   ├── IDpearls/                 # Teaching images
│   └── lectures/                 # Fellow presentations
├── case_presentations/           # Conference materials
└── claude.md                     # Claude's operational instructions
```

---

## 🤖 How It Works

### Claude Code's Role

Claude Code handles the heavy lifting:
1. **Research**: Searches PubMed, IDSA guidelines, CDC resources for evidence-based content
2. **Synthesis**: Integrates multiple sources into concise, fellow-level cards
3. **Enhancement**: Creates mnemonics, downloads teaching images, formats tables
4. **Optimization**: Converts markdown to Anki-compatible HTML with proper typography
5. **Learning**: Analyzes git diffs to understand user preferences and improve future cards
6. **Monitoring**: Watches for new PDFs, user edits, and feedback to trigger card generation

### User's Role

The ID fellow provides:
- New literature (drop PDFs into `articles/`)
- Feedback on card quality (edit markdown files, commit changes)
- Topic requests (mention specific areas for expansion)
- Manual image downloads (Febrile Podcast, X.com infographics when needed)

**The collaboration:** User curates content → Claude generates cards → User refines → Claude learns

---

## 🎓 Card Design Philosophy

Every card includes:
- **Evidence-based content** from ≥2 primary sources
- **Mnemonic** or memory aid (top priority)
- **Clinical reasoning** (pattern recognition, distinguishing features)
- **Visual element** (table, figure, or diagram when possible)
- **Specific citations** (not generic textbook references)

**Example Card:**
```markdown
**Q:** What are the key features differentiating mucormycosis from aspergillosis?

**A:**
| Feature | Mucormycosis | Aspergillosis |
|---------|--------------|---------------|
| Histology | Broad (5-20 μm), non-septate, 90° branching | Narrow (2-5 μm), septate, 45° branching |
| Risk | DKA (most important), deferoxamine | Neutropenia, HSCT |
| Hallmark | Angioinvasion → black necrotic eschar | Angioinvasion → hemoptysis, cavitation |
| Treatment | Amphotericin B + aggressive surgical debridement | Voriconazole OR amphotericin B |

**Mnemonic:** "Mucor Munches vessels at 90° angles"

**Sources:** [IDSA Fungal Guidelines 2024], [PMC7123456]
```

---

## 📥 Getting Started

### Import to Anki

1. **Download the latest deck:**
   ```
   Anki_Deck_Generator/generated_decks/ID_deck_2025-11-12.tsv
   ```

2. **Import to Anki:**
   - Open Anki → File → Import
   - Select the TSV file
   - Field mapping: Front | Back | Tags
   - Import as "Basic" note type
   - Destination deck: "Infectious Diseases"

3. **Start studying!**
   - 503 cards ready for spaced repetition
   - Optimized for night mode
   - Clean typography (19px questions, 16px answers)

### Generate New Cards

```bash
# Add new PDF to articles/ → Claude detects and generates cards

# Edit existing card → Claude learns from your changes
git add Anki_Deck_Generator/cards/
git commit -m "Refined blastomycosis card"

# Regenerate deck after edits
cd Anki_Deck_Generator
python3 convert_to_anki.py
```

---

## 📚 Content Sources

**Primary Literature (Priority 1):**
- PubMed searches (clinical trials, systematic reviews)
- IDSA clinical practice guidelines
- CDC recommendations
- High-impact journals (NEJM, JAMA, Lancet, CID)

**Repository PDFs (Priority 2):**
- 63 curated papers in `articles/`
- 28 syndrome-focused papers in `notes/Lessons_of_Stout/`

**Medical Education Sites (Priority 3):**
- IBCC/EMCrit (ID and ICU content)
- WikEM (emergency medicine perspective)
- Life in the Fast Lane (clinical pearls)

**Supplementary:**
- Febrile Podcast infographics
- X.com ID educators (@1min_IDconsult, @ABsteward)

---

## 🔧 Technical Details

### Typography Optimization
- Questions: 19px, font-weight 500 (prominent)
- Answers: 16px, font-weight 400, antialiased (readable)
- Tables: 14px, dark blue headers (#2c5aa0) for night mode
- Headers: h1=19px, h2=18px, h3=17px, h4=16px
- Compact spacing (line-height 1.3-1.4)

### Conversion Features
- Markdown → HTML: Bold, italic, tables, lists, headers, images
- Table rendering: Proper borders, collapse, night-mode compatible
- Image handling: Automatic `<img>` tag conversion
- Whitespace cleanup: Max 2 consecutive `<br>` tags
- TSV export: Front | Back | Tags (3 columns)

### Version Control
- Git-enabled repository
- Claude learns from commit diffs
- User edits → automatic preference learning
- No manual feedback documentation needed

---

## 🏆 Achievements

**By Claude Code:**
- ✅ Researched and synthesized 503 evidence-based cards
- ✅ Integrated content from 63+ PDFs and 100+ online sources
- ✅ Created mnemonics and memory aids for every major topic
- ✅ Downloaded teaching images from IBCC, PMC, and educational sites
- ✅ Built and optimized markdown → Anki conversion pipeline
- ✅ Implemented night mode compatibility and typography optimization
- ✅ Established continuous monitoring for new content
- ✅ Documented complete workflow for sustainability

**By ID Fellow:**
- ✅ Curated 63 primary literature PDFs
- ✅ Provided feedback on card quality and detail level
- ✅ Organized educational resources by syndrome
- ✅ Refined cards through iterative editing

---

## 🚀 Future Work

**Continuous Expansion:**
- New cards triggered by PDF additions
- Updates when guidelines are revised
- Expansion of specific topics based on user feedback

**Ongoing Optimization:**
- Learning from user edits via git diffs
- Refining mnemonics based on retention data
- Adding more teaching images as sources become available

---

## 📄 License & Attribution

**Content:** Synthesized from publicly available guidelines, peer-reviewed literature, and medical education resources. All sources cited in individual cards.

**Code:** Conversion scripts and workflows developed by Claude Code (Anthropic) in collaboration with ID fellowship curriculum development.

**Heavy Lifting:** Claude Code handled research, synthesis, card generation, image retrieval, conversion optimization, and documentation. The ID fellow provided curation, feedback, and clinical expertise.

---

## 📞 Contact

For questions about card content, suggest topics for expansion, or report issues with the conversion pipeline.

**Repository maintained collaboratively:**
- **Content Curation:** ID Fellow
- **Card Generation & Technical Infrastructure:** Claude Code (Anthropic)

---

**Current Version:** 503 cards | Last Updated: 2025-11-12 | Deck: `ID_deck_2025-11-12.tsv`
