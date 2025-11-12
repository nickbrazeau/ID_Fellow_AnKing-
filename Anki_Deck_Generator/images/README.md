# Images Directory

This directory stores mnemonics, schematics, and infographics for Anki cards.

## Image Generation Capability

Claude can:

1. **Generate simple mnemonic images** using Python PIL/Pillow (requires installation)
2. **Download images from web sources** when URLs are accessible
3. **Create text-based visual aids** for tables and mnemonics
4. **Extract figures from PDFs** in your repository

## Current Limitations Encountered

- **PIL/Pillow not installed**: Install with `pip install Pillow` to enable image generation
- **X.com/Twitter access**: Requires authentication, cannot scrape directly
- **Notion pages**: Require authentication for access

## Working Around Limitations

**For immediate use:**
- Reference images by filename in cards
- Manually add images from:
  - Screenshots from Febrile Podcast
  - Downloaded figures from @1min_IDconsult (save as PNG)
  - Extracted images from PDFs in `articles/` and `Lessons_of_Stout/`

**Image naming convention:**
- `<topic>_<description>.png`
- Examples:
  - `csf_interpretation_table.png`
  - `duke_criteria_major_minor.png`
  - `carbapenem_spectrum_venn.png`
  - `hacek_mnemonic.png`

## Recommended Images to Add Manually

Based on the cards generated:

1. **CSF interpretation table** - from any meningitis reference
2. **Duke criteria flowchart** - from AHA guidelines
3. **SOT infection timeline** - from transplant ID textbook
4. **HACEK organisms mnemonic** - create or screenshot
5. **Carbapenem spectrum Venn diagram** - from antibiotic guides
6. **Pseudomonas virulence factors schematic** - from microbiology text

Once added, these images will be automatically embedded when converting cards to Anki TSV format.
