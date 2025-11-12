# Content Strategy: Evidence-Based Card Generation

## 🎯 Priority Hierarchy

### 1️⃣ **PRIMARY: Peer-Reviewed Literature & Guidelines**
**Always start here for card content and images**

**Sources (in order):**
- PubMed searches for recent clinical trials, systematic reviews, meta-analyses
- IDSA clinical practice guidelines
- CDC guidelines and recommendations
- WHO and specialty society guidelines (ATS, ESCMID, BSAC, etc.)
- High-impact journals (NEJM, JAMA, Lancet, CID, JID)
- Open-access PMC articles with figures

**Workflow:**
```bash
WebSearch("topic IDSA guideline 2024")
WebSearch("topic systematic review meta-analysis")
WebSearch("topic NEJM JAMA Lancet")
WebSearch("topic figure site:ncbi.nlm.nih.gov/pmc")
```

### 2️⃣ **SECONDARY: Repository PDFs**
**Use your curated literature collection**

- `articles/` - 20+ PDFs including extensive Blastomycosis literature
- `Lessons_of_Stout/` - Organized by syndrome (UTI, PJI, Splenomegaly, PCP)
- Extract figures and key teaching points
- Cite specific papers, not generic textbook chapters

### 3️⃣ **TERTIARY: Medical Education Sites**
**Supplement with teaching diagrams when primary sources lack visuals**

- IBCC/EMCrit (https://emcrit.org/ibcc/) - Excellent ICU/ID content
- WikEM (https://wikem.org) - Emergency medicine perspective
- Life in the Fast Lane (https://lifeinthefastlane.com) - Clinical pearls
- Use for: teaching mnemonics, simplified diagrams, quick reference

**When to use:**
- Primary literature has no suitable figures
- Need teaching diagrams to simplify complex topics
- Looking for memorable mnemonics

### 4️⃣ **OPTIONAL: Manual Downloads**
**Only if essential and not available elsewhere**

- Febrile Podcast infographics (user downloads manually)
- X.com/@1min_IDconsult (screenshots)

---

## 📝 Content Synthesis Approach

### For Each Card:

1. **Search primary literature** (PubMed, guidelines)
2. **Review repository PDFs** on the topic
3. **Synthesize evidence** from multiple sources
4. **Cite specific sources** (not generic textbook chapters)
5. **Add teaching aids** (mnemonics, simplified diagrams) from education sites
6. **Download images** from PMC/guidelines first, then education sites

### Example Workflow:

**Topic: Staphylococcus aureus Bacteremia**

```bash
# Step 1: Search guidelines
WebSearch("Staphylococcus aureus bacteremia IDSA guideline 2024")

# Step 2: Search recent literature
WebSearch("SAB complicated vs uncomplicated clinical trial")
WebSearch("SAB treatment duration systematic review")

# Step 3: Search repository
find articles -iname "*staph*" -o -iname "*SAB*"

# Step 4: Search for images
WebSearch("SAB algorithm site:ncbi.nlm.nih.gov/pmc")
WebSearch("SAB management flowchart IDSA")

# Step 5: Supplement with education sites
WebSearch("SAB site:emcrit.org")

# Step 6: Synthesize into card with mnemonic
```

---

## ⚠️ What to AVOID

❌ **Don't:** Rely solely on IBCC/WikEM without checking primary literature
❌ **Don't:** Cite "Mandell Chapter X" without reading specific content
❌ **Don't:** Use outdated guidelines (check publication year)
❌ **Don't:** Skip image searches - visuals are high priority
❌ **Don't:** Create cards without evidence-based sources

✅ **Do:** Search PubMed/guidelines FIRST
✅ **Do:** Cite specific papers and guidelines
✅ **Do:** Use multiple sources for each card
✅ **Do:** Prioritize open-access PMC figures
✅ **Do:** Supplement with education site mnemonics

---

## 📊 Quality Metrics

Each card should demonstrate:
- ✅ Evidence from ≥2 primary sources (guidelines, trials, reviews)
- ✅ Specific citations (not generic textbooks)
- ✅ Current information (prefer last 3-5 years)
- ✅ Visual aid (figure, algorithm, or mnemonic)
- ✅ Clinical reasoning flow (diagnosis → management → pearls)

---

## 🔄 Continuous Improvement

- Learn from git diffs when user edits cards
- Update cards when new guidelines published
- Refine based on user feedback
- Maintain evidence-based rigor
