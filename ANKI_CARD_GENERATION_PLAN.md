# Anki Card Generation Plan

## ✅ Setup Complete

- [x] Directory structure created
- [x] Markdown-to-TSV conversion script written
- [x] Git repository initialized
- [x] CLAUDE.md documentation updated
- [x] Image retrieval capabilities tested
- [x] Example cards created (7 cards in temp_review/)

## 📊 Current Status

### Working Image Sources
✅ **IBCC/EMCrit** - Fully automated downloads
✅ **WikEM** - Likely works (not yet tested)
✅ **Life in the Fast Lane** - Likely works (not yet tested)

### Not Using (Requires Manual Work)
❌ **Febrile Podcast Notion** - Skip (requires manual URL extraction per image)
❌ **X.com/@1min_IDconsult** - Skip (requires authentication)

### Successfully Downloaded Images
- `endocarditis_classic_exam_findings.jpg` (243KB from IBCC)
- `endocarditis_diagnosis_approach.jpg` (296KB from IBCC)

## 🎯 Card Generation Strategy

### Phase 1: Evidence-Based Cards from Primary Literature
**Approach:** Search PubMed, guidelines, and recent publications FIRST, then supplement with medical education sites.

**Workflow for Each Topic:**
1. **WebSearch** for recent guidelines, systematic reviews, clinical trials
2. **WebFetch** guideline documents and open-access papers
3. **Search repository** PDFs (articles/, Lessons_of_Stout/)
4. **Search for images:** PMC open-access figures, guideline algorithms
5. **Supplement** with IBCC/WikEM for teaching diagrams if needed
6. **Synthesize** evidence-based content into cards

Focus on generating cards for high-yield topics:

**Priority Topics (from CLAUDE.md clinical focus areas):**

1. **Antimicrobial Agents** (Chapters 1-40)
   - Beta-lactam spectrum and resistance
   - Carbapenem indications
   - Fluoroquinolone coverage
   - Vancomycin dosing and monitoring
   - Aminoglycoside toxicity

2. **Clinical Syndromes** (Chapters 40-89)
   - Fever of unknown origin
   - Sepsis and septic shock
   - Endocarditis (already started)
   - Meningitis (CSF interpretation - already started)
   - Pneumonia (CAP, HAP, VAP)
   - Urinary tract infections
   - Intra-abdominal infections

3. **Organisms** (Chapters 120-273)
   - Staphylococcus aureus (bacteremia, MRSA)
   - Streptococcus pneumoniae
   - Enterobacterales and ESBL
   - Pseudomonas aeruginosa (already started)
   - Candida species
   - Aspergillus species

4. **Host Factors** (Chapters 282-287)
   - Febrile neutropenia (already started)
   - Solid organ transplant infections (already started)
   - HIV/AIDS opportunistic infections
   - Asplenia infections

### Phase 2: Reference Existing Repository Literature
Create cards based on PDFs in:
- `articles/` (especially Blastomycosis literature - 17 PDFs)
- `Lessons_of_Stout/` subdirectories (UTI, PJI, Splenomegaly, PCP)

### Phase 3: Manual Image Integration (Optional)
If user wants Febrile/X.com content:
- User downloads images manually
- Save to `images/` folder
- Create cards referencing those images

## 📝 Card Requirements

Every card must include:
- ✅ **Mnemonic** (when applicable)
- ✅ **Table format** (for test interpretation)
- ✅ **Proper citations** (IBCC, WikEM, PMC, IDSA - NO generic Mandell citations)
- ✅ **Media reference** (even if image not yet downloaded)
- ✅ **Unique ID** and proper categorization
- ✅ **Fact-dense answers** (≤3 sentences)

## 🚀 Next Steps

1. **Initial git commit** - Commit current setup
2. **Generate first batch** - 10-20 cards on high-yield topics with IBCC images
3. **User review** - Get feedback on content, mnemonics, detail level
4. **Iterate based on feedback** - Adjust based on git diffs of user edits
5. **Scale up production** - Generate cards systematically through priority topics

## 📈 Target Metrics

- **Quality over quantity** - Well-crafted mnemonics and clinically relevant
- **Image coverage** - Aim for 50%+ cards with visual aids
- **Topic coverage** - Hit all 296 chapters from Mandell eventually
- **Avoid duplication** - Check prior_decks/ CSV (230 existing cards)

## 🔄 Continuous Improvement

- Review git diffs after user edits to learn preferences
- Adjust mnemonic style based on feedback
- Refine detail level based on what gets edited
- Improve image selection based on user additions/deletions
