# 🚀 START HERE - New Session Checklist

## For Claude: Read This FIRST Every Session

This checklist ensures you have full context, even if you're a brand new Claude instance who has never seen this repository before.

---

## ✅ Pre-Generation Checklist

### **Step 1: Load Conversation Memory**
```bash
cd /Users/nbrazeau/Desktop/ID_Curriculum/Anki_Deck_Generator
cat CONVERSATION_CONTEXT.md
```

**What you'll learn:**
- Full conversation history
- All decisions made
- User preferences and style
- What NOT to do
- Technical details

**Time:** 2-3 minutes to read

---

### **Step 2: Check Current Progress**
```bash
cat SESSION_RESUME.md
```

**What you'll see:**
- Current progress (X/296 cards)
- Where to resume generation
- Recent activity log
- Next card ID to use

**Time:** 30 seconds

---

### **Step 3: Verify System Status**
```bash
python3 session_manager.py
```

**Expected output:**
```
Progress: X/296 (Y%)
Current: [category/topic or None]
Next ID: ###
Resume from: [specific topic]
```

**Time:** 5 seconds

---

### **Step 4: Check Recent User Edits** *(if any commits exist)*
```bash
git log --oneline | head -10
git log -p --follow cards/ | head -200
```

**What to look for:**
- User's editing patterns
- Preferred detail level
- Mnemonic style preferences
- Citation preferences

**Time:** 1-2 minutes *(skip if no commits yet)*

---

### **Step 5: Review Key Documentation** *(if needed)*

Quick references:
- `CLAUDE.md` - Main instructions
- `CONTENT_STRATEGY.md` - Evidence-based approach
- `LONG_TERM_GENERATION_GUIDE.md` - System usage
- `IMAGE_RETRIEVAL_GUIDE.md` - Image download workflows

**Time:** As needed (usually not required every session)

---

## 🎯 You're Ready When You Can Answer:

- [ ] Where am I resuming generation? (from SESSION_RESUME.md)
- [ ] What's the next card ID? (from session_manager.py)
- [ ] What are the content priorities? (PubMed → Repository → IBCC)
- [ ] What must every card include? (mnemonic, citations, images)
- [ ] How do I log progress? (session_manager.py API)
- [ ] What image sources work? (IBCC, WikEM, PMC)
- [ ] What's the user's style? (from CONVERSATION_CONTEXT.md)

---

## 🚀 Start Generating

Once checklist complete:

```python
from session_manager import SessionManager
sm = SessionManager()

# Get resume point
topic = sm.get_resume_point()
print(f"Resuming: {topic}")

# Get next ID
card_id = sm.get_next_card_id()

# Generate card following CONTENT_STRATEGY.md
# 1. Search PubMed/guidelines
# 2. Check repository PDFs
# 3. Search for images
# 4. Create markdown with mnemonic
# 5. Download images

# Log completion
sm.mark_card_completed('category', card_id, 'filename.md')
```

---

## 📋 Quick Reference

### **Card Requirements:**
- ✅ True mnemonic (when applicable)
- ✅ Evidence from ≥2 sources
- ✅ Specific citations (not generic)
- ✅ Visual aid (image/table/mnemonic)
- ✅ ≤3 sentences per answer
- ✅ Table format for test interpretation

### **Content Priority:**
1. 🥇 PubMed, IDSA/CDC guidelines
2. 🥈 Repository PDFs (articles/, Lessons_of_Stout/)
3. 🥉 IBCC/WikEM (supplementary)

### **Image Priority:**
1. 🥇 PMC open-access, guideline algorithms
2. 🥈 IBCC/WikEM teaching diagrams
3. 🥉 Repository PDF extractions

### **Progress Logging:**
```python
# After EVERY card
sm.mark_card_completed(category, card_id, filename)

# Check status anytime
sm.get_progress_summary()
```

---

## ⚠️ Common Mistakes to Avoid

❌ **Starting without reading CONVERSATION_CONTEXT.md**
→ You'll miss critical decisions and preferences

❌ **Skipping SESSION_RESUME.md**
→ You'll start from wrong topic

❌ **Not checking git log**
→ You'll miss user's style preferences

❌ **Forgetting to log progress**
→ Next session won't know what was completed

❌ **Using generic citations**
→ User specifically requested specific sources

❌ **Skipping primary literature search**
→ User wants PubMed/guidelines FIRST, not just IBCC

✅ **Do the checklist every single session**
✅ **Read CONVERSATION_CONTEXT.md completely**
✅ **Follow evidence-based workflow**
✅ **Log progress after each card**

---

## 🔄 If Something Seems Wrong

### **Lost context?**
→ Read CONVERSATION_CONTEXT.md again completely

### **Unsure where to resume?**
→ Check SESSION_RESUME.md and run session_manager.py

### **Card ID seems wrong?**
→ Check progress_tracker.json "next_id" field

### **Need to restart from topic?**
→ Edit progress_tracker.json "current_topic" field

### **System behaving oddly?**
→ Read LONG_TERM_GENERATION_GUIDE.md troubleshooting section

---

## ✅ Completion

Once you've completed the checklist:
1. You understand the full context
2. You know where to resume
3. You know the user's preferences
4. You're ready to generate high-quality cards

**Total time: 5-10 minutes per session**

**This investment ensures continuity across terminal losses!**

---

## 📝 End of Session

Before you finish:
1. Ensure all cards logged with `sm.mark_card_completed()`
2. Progress auto-saved automatically
3. SESSION_RESUME.md auto-updated
4. Ready for next session!

No need to manually save anything - system handles it.
