# Image Retrieval Solutions for Anki Card Generation

## ✅ **WORKING SOLUTIONS**

### **1. Direct Image URLs from Medical Education Sites**

**Success:** Can download images directly via `curl` from sites that serve static images.

**Tested & Working Sources:**
- **IBCC/EMCrit** (https://emcrit.org/ibcc/) - ✅ Works perfectly
- Example images downloaded:
  - `endocarditis_classic_exam_findings.jpg` (243KB)
  - `endocarditis_diagnosis_approach.jpg` (296KB)

**Command:**
```bash
curl -o images/<filename>.jpg "<image_url>"
```

**Other Likely Working Sources:**
- WikEM (https://wikem.org)
- Life in the Fast Lane (https://lifeinthefastlane.com)
- Radiopaedia (https://radiopaedia.org)
- NEJM Images in Clinical Medicine (if publicly accessible)

### **2. Web Search → Find Direct Image URLs**

**Workflow:**
1. Use WebSearch to find relevant content
2. Use WebFetch to extract image URLs from HTML
3. Download with curl command

**Example:**
```bash
# Step 1: Search
WebSearch("CSF interpretation table meningitis")

# Step 2: Extract URLs from promising pages
WebFetch("https://site.com/article")

# Step 3: Download
curl -o images/csf_table.jpg "https://site.com/image.jpg"
```

---

## ⚠️ **PARTIALLY WORKING (Requires User Assistance)**

### **1. Febrile Podcast Notion Library**
- **Status:** ✅ CAN download IF given full Notion proxy URLs
- **How it works:**
  - Direct S3 URLs: ❌ Access Denied
  - Notion proxy URLs: ✅ Works perfectly
  - Format needed: `https://sarawinndong.notion.site/image/https%3A%2F%2Fprod-files-secure.s3...`
- **Workflow:**
  - User browses Notion library in browser
  - User right-clicks image → "Copy image address"
  - User provides URL to Claude
  - Claude downloads with curl
- **Decision:** Skipping for now - requires too much manual URL extraction per image
- **Alternative:** User can manually download and save to `images/` folder

### **2. X.com/Twitter (@1min_IDconsult)**
- **Issue:** Requires JavaScript + authentication for content
- **Status:** ❌ Cannot access tweet content or images
- **Workaround:** Manual download or screenshot by user

### **3. Protected Medical Journals**
- Most require institutional access or subscription

---

## 📋 **RECOMMENDED WORKFLOW (PRIORITY ORDER)**

### **For Each Card Generation Session:**

1. **Search for evidence-based images FIRST:**
   ```bash
   # PubMed Central open-access figures
   WebSearch("<topic> figure site:ncbi.nlm.nih.gov/pmc")

   # Clinical guidelines with algorithms
   WebSearch("<topic> IDSA guideline algorithm flowchart")
   WebSearch("<topic> CDC guideline")

   # Recent publications with figures
   WebSearch("<topic> NEJM figure")
   WebSearch("<topic> clinical review diagram")
   ```

2. **Supplement with medical education sites:**
   ```bash
   WebSearch("<topic> diagram site:emcrit.org OR site:wikem.org")
   WebSearch("<topic> mnemonic site:lifeinthefastlane.com")
   ```

3. **Extract image URLs:**
   ```bash
   WebFetch("https://page-url") → look for image URLs
   ```

4. **Download images:**
   ```bash
   curl -o images/<descriptive_name>.jpg "<url>"
   ```

5. **If not available publicly:**
   - Document needed image in card as: `images/<topic>_<description>.png`
   - Add to "MANUAL DOWNLOAD LIST" below
   - User can add manually later

---

## 📝 **MANUAL DOWNLOAD STRATEGY**

Since Febrile Podcast and X.com require manual intervention, focus on these approaches:

### **Primary Strategy: Evidence-Based Literature Search**
✅ Search PubMed/PMC and guidelines FIRST for figures
- Open-access PMC articles often have downloadable figures
- IDSA/CDC guidelines frequently include algorithms and flowcharts
- Priority: Evidence-based content over educational summaries

### **Secondary Strategy: Medical Education Sites (Automated)**
✅ Use IBCC/WikEM/LITFL for teaching diagrams when primary literature lacks visuals
- These sites are excellent for summary diagrams and mnemonics
- Should supplement, not replace, primary literature

### **Tertiary Strategy: Repository PDFs**
- Extract figures from PDFs in `articles/` and `Lessons_of_Stout/`
- Use PDF tools or screenshots
- Save to `images/` folder

### **Optional: Manual User Downloads**
If specific Febrile/X.com images are essential:

**From Febrile Podcast Notion Library:**
1. Browse to: https://sarawinndong.notion.site/Welcome-to-the-Febrile-ID-infographic-library-1c9af087a5314101a00bccacac0dd164
2. Right-click image → "Save image as..."
3. Save to: `Anki_Deck_Generator/images/febrile_<topic>.png`

**From @1min_IDconsult (X.com):**
1. Browse to: https://x.com/1min_IDconsult
2. Screenshot or save image
3. Save to: `Anki_Deck_Generator/images/1minID_<topic>.png`

---

## 🎯 **BEST PRACTICES**

1. **Always try IBCC/EMCrit first** - Most reliable for ID content
2. **Name files descriptively:** `<topic>_<description>.jpg`
3. **Check image before using:** Verify download with `ls -lh images/`
4. **Cite source in card:** Include [IBCC], [WikEM], etc.
5. **For unavailable images:** Reference filename anyway - user can add later

---

## 🔧 **Technical Commands Reference**

```bash
# Search for image
WebSearch("topic mnemonic diagram site:emcrit.org")

# Extract URLs from page
WebFetch("https://site.com/page")

# Download image
curl -o images/filename.jpg "https://site.com/image.jpg"

# Verify download
ls -lh images/filename.jpg

# View image (macOS)
open images/filename.jpg
```

---

## ✨ **SUCCESS EXAMPLE**

Created card `syndromes_endocarditis-physical-exam_009.md` with:
- Real downloaded image from IBCC
- Mnemonic: "OSLER is OUCH" vs "Janeway is JUST there"
- Properly formatted Media field
- Working image reference: `images/endocarditis_classic_exam_findings.jpg`

This proves the workflow works end-to-end!
