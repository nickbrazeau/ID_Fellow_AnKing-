# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an **Infectious Diseases (ID) fellowship curriculum repository** containing educational materials, case presentations, medical literature, and tools for generating Anki flashcards. The primary focus is creating high-yield study materials for ID fellows through systematic synthesis of evidence-based resources.

### **IMPORTANT: At Start of Each Session**

**Before generating any cards, ALWAYS read these files in order:**
1. **`Anki_Deck_Generator/CONVERSATION_CONTEXT.md`** - Full conversation history, decisions, user preferences
2. **`Anki_Deck_Generator/SESSION_RESUME.md`** - Current progress and where to resume
3. Check progress: `cd Anki_Deck_Generator && python3 session_manager.py`
4. Check recent edits: `git log -p --follow Anki_Deck_Generator/cards/ | head -200`
5. Resume from the indicated topic
6. Use session_manager.py to track progress after each card

**These files preserve ALL context across terminal/session losses.** Reading them ensures continuity even if you're a completely new Claude instance.

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

## 🎓 Key Clinical Focus Areas

- ## Antimicrobial Agents

  1. Molecular Mechanisms of Antibiotic Resistance in Bacteria
  2. Pharmacokinetics and Pharmacodynamics of Antiinfective Agents
  3. Penicillins and β-Lactamase Inhibitors
  4. Cephalosporins and Cephalosporin/β-Lactamase Inhibitor Combinations
  5. Carbapenems, Carbapenem/β-Lactamase Inhibitor Combinations, and Aztreonam
  6. Antibiotic Allergy
  7. Aminoglycosides
  8. Tetracyclines, Tetracycline Derivatives, and Chloramphenicol
  9. Rifamycins
  10. Metronidazole
  11. Macrolides and Clindamycin
  12. Glycopeptides (Vancomycin and Teicoplanin) and Lipoglycopeptides (Telavancin, Oritavancin, Dalbavancin)
  13. Streptogramins (Quinupristin-Dalfopristin) and Lipopeptides (Daptomycin)
  14. Polymyxins (Polymyxin B and Colistin)
  15. Linezolid, Tedizolid, and Other Oxazolidinones
  16. Sulfonamides and Trimethoprim; Trimethoprim-Sulfamethoxazole
  17. Quinolones
  18. Antibiotics in Advanced Development and Other Agents
  19. Urinary Tract Agents: Nitrofurantoin, Fosfomycin, and Methenamine
  20. Topical Antibacterials
  21. Antimycobacterial Agents
  22. Bacteriophage Therapy, Endolysin Therapy, and Antimicrobial Peptide Therapy
  23. Antifungal Agents: Polyene Antifungals
  24. Antifungal Drugs: Azoles
  25. Antifungal Drugs: Echinocandins and Other Beta-d-Glucan Inhibitors
  26. Antifungal Drugs: Flucytosine
  27. Antimalarial Drugs
  28. Drugs for Protozoal Infections Other Than Malaria
  29. Drugs for Helminths
  30. Antiviral Agents: General Principles
  31. Antiviral Drugs for Influenza and Other Respiratory Virus Infections (Except SARS-CoV-2)
  32. Antivirals Against Herpesviruses
  33. Antiviral Drugs Against Hepatitis Viruses
  34. Miscellaneous Antiviral Agents (Interferons, Tecovirimat, Imiquimod, Pocapavir)
  35. Immunomodulators
  36. Hyperbaric Oxygen
  37. Antibiotic Stewardship
  38. Designing and Interpreting Clinical Studies in Infectious Diseases
  39. Outpatient Parenteral Antimicrobial Therapy
  40. Temperature Regulation and the Pathogenesis of Fever
  41. Fever of Unknown Origin
  42. The Acutely Ill Patient With Fever and Rash
  43. The Common Cold
  44. Pharyngitis
  45. Acute Laryngitis
  46. Otitis Externa, Otitis Media, and Mastoiditis
  47. Sinusitis
  48. Epiglottitis
  49. Infections of the Oral Cavity, Neck, and Head
  50. Acute Bronchitis
  51. Acute Exacerbations of Chronic Obstructive Pulmonary Disease
  52. Acute Pneumonia
  53. Pleural Effusion and Empyema
  54. Bacterial Lung Abscess
  55. Chronic Pneumonia
  56. Cystic Fibrosis
  57. Urinary Tract Infections
  58. Sepsis and Septic Shock
  59. Peritonitis and Intraperitoneal Abscesses
  60. Infections of the Liver and Biliary System (Liver Abscess, Cholangitis, Cholecystitis)
  61. Pancreatic Infection
  62. Splenic Abscess
  63. Appendicitis
  64. Diverticulitis and Neutropenic Enterocolitis
  65. Endocarditis and Intravascular Infections
  66. Prosthetic Valve Endocarditis
  67. Infections of Nonvalvular Cardiovascular Devices
  68. Prevention of Infective Endocarditis
  69. Myocarditis and Pericarditis
  70. Mediastinitis
  71. Acute Meningitis
  72. Chronic Meningitis
  73. Encephalitis
  74. Brain Abscess
  75. Subdural Empyema, Epidural Abscess, and Suppurative Intracranial Thrombophlebitis
  76. Cerebrospinal Fluid Shunt and Drain Infections
  77. Cellulitis, Necrotizing Fasciitis, and Subcutaneous Tissue Infections
  78. Myositis and Myonecrosis
  79. Lymphadenitis and Lymphangitis
  80. Syndromes of Enteric Infection
  81. Esophagitis
  82. Diarrhea With Little or No Fever
  83. Acute Dysentery Syndromes (Diarrhea With Fever)
  84. Typhoid Fever, Paratyphoid Fever, and Typhoidal Fevers
  85. Foodborne Disease (Food Poisoning)
  86. Tropical Sprue and Environmental Enteric Dysfunction
  87. Infectious Arthritis of Native Joints
  88. Osteomyelitis
  89. Orthopedic Implant–Associated Infections
  90. Anogenital Skin and Mucous Membrane Lesions
  91. Urethritis
  92. Vulvovaginitis and Cervicitis
  93. Infections of the Female Pelvis
  94. Prostatitis, Epididymitis, and Orchitis
  95. Microbial Conjunctivitis
  96. Microbial Keratitis
  97. Endophthalmitis
  98. Infectious Causes of Uveitis
  99. Periocular Infections
  100. Viral Hepatitis
  101. Human Immunodeficiency Viruses
  102. Global Perspectives on HIV Infection and AIDS
  103. Epidemiology and Prevention of HIV/AIDS (Including PrEP and Vaccine Development)
  104. Diagnosis of HIV Infection
  105. Immunology and Viral Persistence in HIV
  106. Clinical Manifestations of HIV Infection
  107. Pulmonary Manifestations of HIV Infection
  108. Gastrointestinal, Hepatobiliary, and Pancreatic Manifestations of HIV
  109. Neurologic Diseases in HIV
  110. Pediatric HIV Infection
  111. Antiretroviral Therapy for HIV
  112. Management of Opportunistic Infections in HIV
  113. SARS-CoV-2 Virology
  114. Global Perspective and Epidemiology of COVID-19
  115. Immunology and Diagnosis of COVID-19
  116. Clinical Manifestations of COVID-19 in Adults and Children
  117. Treatment and Prevention of COVID-19
  118. Myalgic Encephalomyelitis / Chronic Fatigue Syndrome
  119. Biology of Viruses and Viral Diseases
  120. Orthopoxviruses (Vaccinia, Variola, Mpox, Cowpox)
  121. Other Poxviruses (Parapoxviruses, Molluscum Contagiosum, Yatapoxviruses)
  122. Herpes Simplex Virus
  123. Varicella-Zoster Virus (Chickenpox and Shingles)
  124. Cytomegalovirus
  125. Epstein-Barr Virus
  126. Human Herpesvirus 6 and 7 (Exanthem Subitum)
  127. Kaposi Sarcoma–Associated Herpesvirus (HHV-8)
  128. Herpes B Virus
  129. Adenoviruses
  130. Papillomaviruses
  131. Polyomaviruses (JC, BK, Merkel Cell)
  132. Hepatitis B Virus
  133. Hepatitis D Virus
  134. Human Parvoviruses and Related Viruses
  135. Orthoreoviruses and Orbiviruses
  136. Coltiviruses (Colorado Tick Fever) and Seadornaviruses
  137. Rotaviruses
  138. Alphaviruses
  139. Rubella Virus
  140. Flaviviruses (Dengue, Yellow Fever, West Nile, Zika, etc.)
  141. Hepatitis C
  142. Coronaviruses (SARS, MERS)
  143. Parainfluenza Viruses
  144. Mumps Virus
  145. Respiratory Syncytial Virus
  146. Human Metapneumovirus
  147. Measles Virus
  148. Zoonotic Paramyxoviruses (Nipah, Hendra)
  149. Vesicular Stomatitis Virus and Related Vesiculoviruses
  150. Rabies (Rhabdoviruses)
  151. Marburg and Ebola Virus Diseases
  152. Influenza Viruses (Including Avian and Swine)
  153. Bunyaviruses (Hantavirus, Rift Valley Fever, etc.)
  154. Arenaviruses (Lassa, Junin, Machupo, etc.)
  155. Human T-Lymphotropic Virus
  156. Poliovirus
  157. Coxsackie, Echo, and Numbered Enteroviruses
  158. Human Parechoviruses
  159. Hepatitis A Virus
  160. Rhinovirus
  161. Noroviruses and Sapoviruses
  162. Astroviruses and Picobirnaviruses
  163. Hepatitis E Virus
  164. Prions and Prion Diseases of the CNS
  165. Chlamydia trachomatis
  166. Psittacosis (Chlamydia psittaci)
  167. Chlamydia pneumoniae
  168. Mycoplasma pneumoniae
  169. Genital Mycoplasmas (M. genitalium, M. hominis, Ureaplasma)
  170. Rickettsia rickettsii and Other Spotted Fever Group Rickettsiae
  171. Coxiella burnetii (Q Fever)
  172. Rickettsia prowazekii (Epidemic Typhus)
  173. Rickettsia typhi (Murine Typhus)
  174. Orientia tsutsugamushi (Scrub Typhus)
  175. Ehrlichia chaffeensis, Anaplasma phagocytophilum, and Other Anaplasmataceae
  176. Staphylococcus aureus
  177. Coagulase-Negative Staphylococci
  178. Streptococcus Classification and Group A Streptococcus
  179. Poststreptococcal Sequelae: Rheumatic Fever and Glomerulonephritis
  180. Streptococcus pneumoniae
  181. Enterococcus Species and Related Streptococci
  182. Group B Streptococcus (S. agalactiae)
  183. Viridans and Nutritionally Variant Streptococci
  184. Streptococcus anginosus Group
  185. Corynebacterium diphtheriae
  186. Other Coryneform Bacteria and Rhodococci
  187. Listeria monocytogenes
  188. Bacillus anthracis (Anthrax)
  189. Other Bacillus Species
  190. Erysipelothrix rhusiopathiae
  191. Whipple Disease
  192. Neisseria meningitidis
  193. Neisseria gonorrhoeae
  194. Moraxella catarrhalis, Kingella, and Other Gram-Negative Cocci
  195. Vibrio cholerae
  196. Other Pathogenic Vibrios
  197. Campylobacter jejuni and Related Species
  198. Helicobacter pylori and Other Gastric Helicobacter Species
  199. Enterobacterales (Enterobacteriaceae)
  200. Pseudomonas aeruginosa and Other Pseudomonas Species
  201. Stenotrophomonas maltophilia and Burkholderia cepacia Complex
  202. Burkholderia pseudomallei and Burkholderia mallei (Melioidosis and Glanders)
  203. Acinetobacter Species
  204. Salmonella Species
  205. Bacillary Dysentery (Shigella and Enteroinvasive Escherichia coli)
  206. Haemophilus Species (Including H. influenzae and H. ducreyi)
  207. Brucellosis (Brucella Species)
  208. Francisella tularensis (Tularemia)
  209. Pasteurella Species
  210. Plague (Yersinia pestis)
  211. Yersinia enterocolitica and Yersinia pseudotuberculosis
  212. Bordetella pertussis
  213. Rat-Bite Fever (Streptobacillus moniliformis and Spirillum minus)
  214. Legionnaires' Disease and Pontiac Fever
  215. Capnocytophaga Species
  216. Bartonella (Including Cat-Scratch Disease)
  217. Klebsiella granulomatis (Donovanosis, Granuloma Inguinale)
  218. Other Gram-Negative and Gram-Variable Bacilli
  219. Syphilis (Treponema pallidum)
  220. Endemic Treponematoses
  221. Leptospira Species (Leptospirosis)
  222. Relapsing Fever (Borrelia Species)
  223. Lyme Disease (Borrelia burgdorferi)
  224. Anaerobic Infections: General Concepts
  225. Clostridioides difficile Infection
  226. Tetanus (Clostridium tetani)
  227. Botulism (Clostridium botulinum)
  228. Diseases Caused by Clostridium Species
  229. Bacteroides, Prevotella, Porphyromonas, and Fusobacterium Species
  230. Anaerobic Cocci and Gram-Positive Nonsporulating Bacilli
  231. Mycobacterium tuberculosis
  232. Leprosy (Mycobacterium leprae)
  233. Mycobacterium avium Complex
  234. Nontuberculous Mycobacteria (Other than MAC)
  235. Nocardia Species
  236. Actinomycosis
  237. Candida Species
  238. Aspergillus Species
  239. Mucormycosis and Entomophthoramycosis
  240. Sporothrix schenckii
  241. Chromoblastomycosis
  242. Mycetoma
  243. Cryptococcosis (C. neoformans and C. gattii)
  244. Histoplasmosis
  245. Blastomycosis
  246. Coccidioidomycosis
  247. Dermatophytosis and Other Superficial Mycoses
  248. Paracoccidioidomycosis
  249. Uncommon Fungi and Related Species
  250. Pneumocystis Species
  251. Microsporidiosis
  252. Entamoeba Species (Amebic Colitis and Liver Abscess)
  253. Free-Living Amebae
  254. Malaria (Plasmodium Species)
  255. Leishmania Species
  256. Trypanosoma Species (Chagas Disease)
  257. African Trypanosomiasis (Sleeping Sickness)
  258. Toxoplasma gondii
  259. Giardia lamblia
  260. Trichomonas vaginalis
  261. Babesia Species
  262. Cryptosporidium Species
  263. Cyclospora, Cystoisospora, Sarcocystis, Balantidium, and Blastocystis
  264. Cyanobacteria and Harmful Algal Bloom Illnesses
  265. Intestinal Nematodes (Roundworms)
  266. Tissue Nematodes (Trichinellosis, Filariases, etc.)
  267. Trematodes (Flukes)
  268. Tapeworms (Cestodes)
  269. Visceral Larva Migrans and Uncommon Helminth Infections
  270. Lice (Pediculosis)
  271. Scabies
  272. Myiasis and Tungiasis
  273. Mites (Including Chiggers)
  274. Ticks and Tick Paralysis
  275. Kawasaki Disease
  276. Infection Prevention and Control in Health Care Settings
  277. Disinfection, Sterilization, and Hospital Waste
  278. Infections Caused by Intravascular Devices
  279. Nosocomial Pneumonia
  280. Catheter-Associated Urinary Tract Infection (CAUTI) and Asymptomatic Bacteriuria
  281. Transfusion- and Transplant-Transmitted Infections
  282. Infections in the Immunocompromised Host: General Principles
  283. Prophylaxis and Empirical Therapy in Cancer Patients
  284. Infections in Hematopoietic Cell Transplantation and Cellular Therapies
  285. Infections in Solid Organ Transplant Recipients
  286. Infections in Older Adults
  287. Infections in Asplenic Patients
  288. Infections in Persons Who Inject Drugs
  289. Surgical Site Infections and Antimicrobial Prophylaxis
  290. Burns
  291. Infections Following Trauma Injuries
  292. Bites
  293. Immunizations for Specific Infections
  294. Protection of Travelers
  295. Infections in Returning Travelers
  296. Zoonoses 

---

## ⚠️ Important Notes

- **Environment**: macOS system (Darwin 24.5.0) 
- **File formats**: Expect PDFs, PowerPoint (.pptx), Word (.docx), images (JPEG/PNG), CSV, Excel
- **Accuracy paramount**: All content is clinical/educational - maintain evidence-based accuracy and cite sources
- **Check before creating**: Always review `Anki_Deck_Generator/prior_decks/` before generating new cards to avoid duplication. It is encouraged to edit cards or split cards with new information (eg make 2 cards from a prior single card with additional details)