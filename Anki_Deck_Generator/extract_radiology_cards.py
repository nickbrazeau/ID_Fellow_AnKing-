#!/usr/bin/env python3
"""
Extract ID-relevant cards from Radiology Core.apkg

This script:
1. Extracts the .apkg file (ZIP format containing SQLite database)
2. Queries the Anki database for cards
3. Filters for infectious disease-relevant content
4. Exports to markdown format for review
"""

import sqlite3
import zipfile
import os
import re
import json
from pathlib import Path

# ID-related keywords to filter cards
ID_KEYWORDS = [
    # General terms
    'infection', 'infectious', 'abscess', 'empyema', 'septic',
    'osteomyelitis', 'discitis', 'septic arthritis',

    # Pulmonary
    'pneumonia', 'consolidation', 'cavitation', 'tuberculosis', 'tb',
    'tree-in-bud', 'miliary', 'aspergillosis', 'fungal ball',
    'air crescent', 'halo sign', 'pneumatocele',

    # CNS
    'meningitis', 'encephalitis', 'brain abscess', 'subdural empyema',
    'epidural abscess', 'ventriculitis',

    # Cardiac
    'endocarditis', 'myocarditis', 'pericarditis', 'pericardial effusion',

    # Abdominal
    'cholecystitis', 'cholangitis', 'appendicitis', 'diverticulitis',
    'liver abscess', 'splenic abscess', 'pyelonephritis',
    'perinephric abscess', 'psoas abscess',

    # Specific organisms
    'staph', 'staphylococcus', 'strep', 'streptococcus',
    'aspergillus', 'cryptococcus', 'candida', 'mucor',
    'histoplasma', 'coccidioides', 'blastomyces',
    'echinococcus', 'hydatid',

    # MSK
    'osteomyelitis', 'septic joint', 'brodie', 'sequestrum',
    'involucrum', 'periostitis',
]

def extract_apkg(apkg_path, extract_dir):
    """Extract .apkg file to directory"""
    print(f"Extracting {apkg_path}...")
    with zipfile.ZipFile(apkg_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print(f"Extracted to {extract_dir}")

def query_cards(db_path):
    """Query all cards from Anki database"""
    print(f"Querying database: {db_path}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Anki database structure:
    # notes table contains the card content
    # cards table links to notes
    query = """
    SELECT
        n.id as note_id,
        n.flds as fields,
        n.tags as tags,
        c.id as card_id
    FROM notes n
    JOIN cards c ON c.nid = n.id
    """

    cursor.execute(query)
    cards = cursor.fetchall()
    conn.close()

    print(f"Found {len(cards)} total cards")
    return cards

def filter_id_cards(cards):
    """Filter cards for ID-relevant content"""
    print("Filtering for ID-relevant cards...")
    id_cards = []

    for card in cards:
        note_id, fields, tags, card_id = card

        # Fields are separated by \x1f in Anki
        fields_list = fields.split('\x1f')
        all_text = ' '.join(fields_list).lower()
        tags_text = tags.lower()

        # Check if any keyword matches
        for keyword in ID_KEYWORDS:
            if keyword.lower() in all_text or keyword.lower() in tags_text:
                id_cards.append({
                    'note_id': note_id,
                    'card_id': card_id,
                    'fields': fields_list,
                    'tags': tags,
                    'matched_keyword': keyword
                })
                break  # Only add once per card

    print(f"Found {len(id_cards)} ID-relevant cards")
    return id_cards

def export_to_markdown(id_cards, output_file):
    """Export filtered cards to markdown for review"""
    print(f"Exporting to {output_file}...")

    with open(output_file, 'w') as f:
        f.write("# ID-Relevant Radiology Cards from Radiology Core.apkg\n\n")
        f.write(f"**Total Cards Found:** {len(id_cards)}\n\n")
        f.write("---\n\n")

        for i, card in enumerate(id_cards, 1):
            f.write(f"## Card {i}\n\n")
            f.write(f"**Note ID:** {card['note_id']}\n")
            f.write(f"**Card ID:** {card['card_id']}\n")
            f.write(f"**Matched Keyword:** {card['matched_keyword']}\n")
            f.write(f"**Tags:** {card['tags']}\n\n")

            # Write fields (typically Front and Back)
            for j, field in enumerate(card['fields']):
                # Remove HTML tags for readability
                clean_field = re.sub('<[^<]+?>', '', field)
                f.write(f"**Field {j+1}:**\n")
                f.write(f"{clean_field[:500]}{'...' if len(clean_field) > 500 else ''}\n\n")

            f.write("---\n\n")

    print(f"Exported {len(id_cards)} cards to {output_file}")

def export_to_json(id_cards, output_file):
    """Export to JSON for programmatic access"""
    print(f"Exporting to {output_file}...")
    with open(output_file, 'w') as f:
        json.dump(id_cards, f, indent=2)
    print(f"Exported {len(id_cards)} cards to {output_file}")

def main():
    # Paths
    apkg_path = Path("prior_decks/Radiology Core.apkg")
    extract_dir = Path("radiology_extraction_temp")
    output_md = Path("radiology_id_cards.md")
    output_json = Path("radiology_id_cards.json")

    # Create extraction directory
    extract_dir.mkdir(exist_ok=True)

    # Extract .apkg
    extract_apkg(apkg_path, extract_dir)

    # Find collection.anki2 database
    db_path = extract_dir / "collection.anki2"
    if not db_path.exists():
        # Try alternative names
        db_path = extract_dir / "collection.anki21"
        if not db_path.exists():
            print("ERROR: Could not find Anki database file")
            return

    # Query all cards
    cards = query_cards(db_path)

    # Filter for ID cards
    id_cards = filter_id_cards(cards)

    # Export
    export_to_markdown(id_cards, output_md)
    export_to_json(id_cards, output_json)

    print("\n=== SUMMARY ===")
    print(f"Total cards in deck: {len(cards)}")
    print(f"ID-relevant cards: {len(id_cards)}")
    print(f"Match rate: {len(id_cards)/len(cards)*100:.1f}%")
    print(f"\nReview the filtered cards in: {output_md}")
    print(f"JSON export: {output_json}")

    # Cleanup
    # import shutil
    # shutil.rmtree(extract_dir)
    # print(f"\nCleaned up temporary directory: {extract_dir}")

if __name__ == "__main__":
    main()
