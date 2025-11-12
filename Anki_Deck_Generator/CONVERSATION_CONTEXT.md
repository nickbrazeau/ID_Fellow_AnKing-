# Conversation Context & Memory

## 🧠 What Claude Needs to Remember Between Sessions

This file captures key decisions, preferences, and context from our conversations so future Claude instances can maintain continuity.

---

## 📅 Session History

### **Session 1: 2025-01-08 - Initial Setup**

#### **What We Built:**
1. ✅ Markdown-based Anki card system
2. ✅ Git repository initialized
3. ✅ Python conversion script (markdown → TSV)
4. ✅ Image downloading capability (IBCC, WikEM work; Febrile/X.com need manual)
5. ✅ Progress tracking system (session_manager.py)
6. ✅ Long-term generation infrastructure

#### **Key Decisions Made:**

**Card Format:**
- ✅ Individual markdown files (NOT CSV)
- ✅ Stored in category subdirectories
- ✅ Unique ID in filename: `<category>_<topic>_<ID>.md`
- ✅ YAML frontmatter with metadata
- ✅ Convert to TSV only for Anki import

**Content Strategy:**
- ✅ **Prioritize evidence-based sources:**
  1. PubMed, IDSA/CDC guidelines (PRIMARY)
  2. Repository PDFs
  3. IBCC/WikEM (supplementary)
- ✅ **NOT solely relying on IBCC/WikEM** - search primary literature first
- ✅ Cite specific sources (no generic "Mandell Chapter X" without details)

**Mnemonics & Images:**
- ✅ **Every card needs a true mnemonic** (when applicable)
- ✅ **Tables for test interpretation** (e.g., CSF interpretation)
- ✅ **Images strongly preferred** - search PMC/guidelines first
- ✅ Download images from working sources automatically
- ✅ Skip Febrile/X.com images (too much manual work)

**Citations:**
- ✅ Remove generic Mandell citations unless specifically reading that chapter
- ✅ Use: [IBCC], [IDSA 2024], [PMC article], specific paper names
- ✅ NOT: [Mandell Chapter 5: Carbapenems] unless specifically referencing it

**Card Quality Requirements:**
- ✅ Fact-dense (≤3 sentences per answer)
- ✅ Clinical reasoning flow (diagnosis → management → pearls)
- ✅ Mnemonics prioritized
- ✅ Visual aids (figures/tables/mnemonics)
- ✅ Evidence from ≥2 sources

#### **User Feedback on Example Cards:**
User reviewed 7 temp cards and requested:
- ✅ Use tables for test interpretation (like CSF card)
- ✅ Add TRUE mnemonics (not just calling something a mnemonic)
- ✅ Add actual media/images
- ✅ Prove ability to download images from web
- ✅ Don't cite Mandell generically

**We addressed all feedback:**
- Updated CSF card with table + BLAST mnemonic
- Added mnemonics to all cards (CAPE, BATES, NSC, BE PHAT)
- Downloaded 2 images from IBCC successfully
- Tested Febrile (works with Notion proxy URLs but skipping)
- Removed generic Mandell citations

#### **Repository Structure Understanding:**
- `articles/` - 20+ PDFs including Blastomycosis lit (17 papers)
- `Lessons_of_Stout/` - Organized by syndrome (UTI, PJI, Splenomegaly, PCP)
- `bugs&drugs/` - Antibiotic dosing guides, PK tables
- `prior_decks/` - Legacy CSV with 230 cards (check for suspended topics, not duplication)

---

## 🎯 User Preferences & Style

### **Content Depth:**
- ID fellow level (assume basic microbiology knowledge)
- Evidence-based, not just educational summaries
- Multiple sources per card
- Recent guidelines (prefer last 3-5 years)

### **Mnemonic Style:**
- Simple, memorable acronyms (BLAST, CAPE, NSC)
- Explained inline with card
- Visual component when possible

### **Image Preferences:**
- PMC/guideline figures > education site diagrams
- Evidence-based over cartoons
- Clinical algorithms and flowcharts valued
- Tables for test interpretation

### **Citation Style:**
- Specific and verifiable
- [IBCC Section Name], [IDSA 2024 Guideline]
- [PMC######] or specific paper titles
- No generic textbook references

---

## 🔄 Long-Term Generation Plan

### **Scope:**
- **296 TOPICS** from Mandell's Principles (all chapters)
- **~1,480 CARDS estimated** (avg 5 cards per topic, range 3-10)
- **7 major categories** organized in progress_tracker.json
- **Multiple sessions** over weeks/months

### **Cards per Topic:**
- Simple topics: 3-5 cards (e.g., single organism)
- Complex topics: 5-10 cards (e.g., syndrome with multiple aspects)
- Average target: 5 cards/topic
- Adjust based on topic complexity and clinical importance

### **Workflow:**
1. **Start session:** Read SESSION_RESUME.md
2. **Check progress:** python3 session_manager.py
3. **Resume from:** Indicated topic
4. **For each card:**
   - Search PubMed/guidelines first
   - Check repository PDFs
   - Search for images (PMC → IBCC)
   - Create markdown with mnemonic
   - Log progress: sm.mark_card_completed()
5. **End session:** Progress auto-saved

### **Git Strategy:**
- Commit every 10-20 cards
- User will edit cards
- Future Claude reads git diffs to learn preferences
- Analyze: `git log -p --follow Anki_Deck_Generator/cards/`

---

## 💡 Technical Details

### **Card ID System:**
- Starts at 10 (IDs 001-009 reserved for examples)
- Auto-increments via session_manager.py
- Never reuse IDs
- Format: 3-digit zero-padded (010, 011, 012...)

### **Image Naming:**
- `<topic>_<description>.png`
- Stored in: `Anki_Deck_Generator/images/`
- Referenced in cards as: `images/filename.png`

### **File Naming:**
- `<category>_<topic>_<ID>.md`
- Category: antimicrobials, syndromes, organisms, host_factors, diagnostics, misc
- Topic: short descriptive name (kebab-case)
- ID: 3-digit (010, 011, 012...)

### **Working Image Sources:**
- ✅ IBCC/EMCrit (emcrit.org/ibcc/)
- ✅ WikEM (wikem.org)
- ✅ LITFL (lifeinthefastlane.com)
- ✅ PMC open-access (ncbi.nlm.nih.gov/pmc)
- ❌ Febrile Notion (requires manual per-image)
- ❌ X.com (requires authentication)

### **Conversion:**
```bash
cd Anki_Deck_Generator
python3 convert_to_anki.py
# Output: generated_decks/ID_deck_YYYY-MM-DD.tsv
```

---

## 🚫 What NOT to Do

❌ Don't rely solely on IBCC/WikEM without checking primary literature
❌ Don't cite "Mandell Chapter X" without reading specific content
❌ Don't create cards without mnemonics (when applicable)
❌ Don't skip image searches - visuals are high priority
❌ Don't duplicate topics from prior_decks/ (230 existing cards are for reference on suspended content)
❌ Don't batch progress updates - log after EACH card
❌ Don't assume Selenium/Pillow/browser automation available (they're not installed)

✅ Do search PubMed/guidelines FIRST
✅ Do cite specific papers and guidelines
✅ Do use multiple sources for each card
✅ Do prioritize open-access PMC figures
✅ Do add true mnemonics with explanation
✅ Do use tables for test interpretation
✅ Do update progress after every single card

---

## 🔍 How to Resume Continuity

### **At Start of EVERY Session:**

1. **Read this file (CONVERSATION_CONTEXT.md)** - Understand full history
2. **Read SESSION_RESUME.md** - See current progress
3. **Run:** `python3 session_manager.py` - Verify status
4. **Check git log:** `git log --oneline | head -10` - See recent commits
5. **If user edited cards:** `git log -p --follow cards/ | head -200` - Learn from edits

### **Questions to Ask Yourself:**
- Where did we leave off? (SESSION_RESUME.md)
- What were the key decisions? (This file, CONVERSATION_CONTEXT.md)
- What's the user's style? (Git diffs of their edits)
- What sources to prioritize? (PubMed → Repository → IBCC)
- Are images needed? (Yes, search PMC/guidelines first)

---

## 📝 Future Sessions: Update This File

When you (future Claude) complete a session:

1. **Add session entry** with date
2. **Note any new decisions** or preferences discovered
3. **Record user feedback** on generated cards
4. **Update style preferences** based on user edits
5. **Save this file** before ending session

### **Template for New Session:**

```markdown
### **Session X: YYYY-MM-DD**

**Cards Generated:** X cards on [topics]

**New Decisions:**
- [Any new preference or approach]

**User Feedback:**
- [What user liked/disliked]

**Lessons Learned:**
- [From git diffs of user edits]
```

---

## 🎊 System Status

**Current State (2025-01-08):**
- ✅ Setup complete
- ✅ 7 example cards in temp_review/
- ✅ 2 images downloaded
- ✅ All systems tested
- ⏳ Awaiting user review of examples
- ⏳ Ready to start systematic generation

**Next Steps:**
1. User reviews 7 example cards
2. Initial git commit
3. Start generating first batch (10-20 cards)
4. User provides feedback
5. Iterate and scale up

---

## 📚 Critical Files to Read Each Session

**Priority Order:**
1. `CONVERSATION_CONTEXT.md` (this file) - Full history
2. `SESSION_RESUME.md` - Current status
3. `CLAUDE.md` - Main instructions
4. `CONTENT_STRATEGY.md` - Evidence-based approach
5. `LONG_TERM_GENERATION_GUIDE.md` - System usage
6. Recent git log - Learn from user edits

**Don't start generating without reading #1 and #2 above!**

---

## 💬 Communication Style

- Professional, concise
- No unnecessary emojis (unless user requests)
- Clear explanations
- Evidence-based approach
- Acknowledge limitations honestly
