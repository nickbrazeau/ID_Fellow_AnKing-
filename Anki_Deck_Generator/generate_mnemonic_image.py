#!/usr/bin/env python3
"""
Simple script to generate mnemonic images for Anki cards using PIL.
This creates basic text-based visual mnemonics.
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("PIL not available. Install with: pip install Pillow")

def create_mnemonic_image(title, mnemonic, description, output_path, width=800, height=600):
    """Create a simple mnemonic image."""
    if not PIL_AVAILABLE:
        print(f"Cannot create image {output_path} - PIL not installed")
        return False

    # Create image with white background
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    # Try to use a better font, fall back to default
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
        mnemonic_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 72)
        desc_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
    except:
        title_font = ImageFont.load_default()
        mnemonic_font = ImageFont.load_default()
        desc_font = ImageFont.load_default()

    # Draw title
    draw.text((width//2, 60), title, fill='black', font=title_font, anchor='mm')

    # Draw mnemonic in center (large)
    draw.text((width//2, height//2 - 50), mnemonic, fill='#2E86AB', font=mnemonic_font, anchor='mm')

    # Draw description (wrap text)
    y_offset = height//2 + 80
    max_width = width - 100
    lines = description.split('\n')
    for line in lines:
        draw.text((width//2, y_offset), line, fill='#555555', font=desc_font, anchor='mm')
        y_offset += 35

    # Save image
    img.save(output_path)
    print(f"Created: {output_path}")
    return True

def create_table_image(title, headers, rows, output_path, width=1000, height=500):
    """Create a simple table image."""
    if not PIL_AVAILABLE:
        print(f"Cannot create image {output_path} - PIL not installed")
        return False

    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
        header_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 22)
        cell_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18)
    except:
        title_font = ImageFont.load_default()
        header_font = ImageFont.load_default()
        cell_font = ImageFont.load_default()

    # Draw title
    draw.text((width//2, 40), title, fill='black', font=title_font, anchor='mm')

    # Table dimensions
    start_y = 100
    row_height = 60
    col_width = (width - 100) // len(headers)

    # Draw headers
    for i, header in enumerate(headers):
        x = 50 + i * col_width + col_width//2
        draw.rectangle([50 + i * col_width, start_y, 50 + (i+1) * col_width, start_y + row_height],
                      outline='black', fill='#E8F4F8', width=2)
        draw.text((x, start_y + row_height//2), header, fill='black', font=header_font, anchor='mm')

    # Draw rows
    for row_idx, row in enumerate(rows):
        y = start_y + (row_idx + 1) * row_height
        for col_idx, cell in enumerate(row):
            x = 50 + col_idx * col_width + col_width//2
            draw.rectangle([50 + col_idx * col_width, y, 50 + (col_idx+1) * col_width, y + row_height],
                          outline='black', width=1)
            # Wrap text if too long
            if len(str(cell)) > 20:
                cell_short = str(cell)[:17] + '...'
            else:
                cell_short = str(cell)
            draw.text((x, y + row_height//2), cell_short, fill='black', font=cell_font, anchor='mm')

    img.save(output_path)
    print(f"Created: {output_path}")
    return True

# Example usage
if __name__ == "__main__":
    import os
    os.makedirs("images", exist_ok=True)

    # CSF table
    create_table_image(
        "CSF Interpretation for Meningitis",
        ["Type", "WBC", "Cell Type", "Glucose", "Protein"],
        [
            ["Bacterial", "1000-5000", "PMN >80%", "<40", ">200"],
            ["Viral", "10-1000", "Lymphs", "Normal", "50-100"],
            ["Fungal/TB", "10-500", "Lymphs", "<45", ">100"]
        ],
        "images/csf_interpretation_table.png"
    )

    # BLAST mnemonic
    create_mnemonic_image(
        "Low CSF Glucose Causes",
        "BLAST",
        "B = Bacterial\nL = Listeria\nA = Amycobacterium (TB)\nS = Syphilis\nT = Tumor/Fungal",
        "images/csf_blast_mnemonic.png"
    )

    # NSC mnemonic
    create_mnemonic_image(
        "SOT Infection Timeline",
        "NSC",
        "N = Nosocomial (<30 days)\nS = Specific/Opportunistic (30-180 days)\nC = Community (>6 months)",
        "images/sot_infection_timeline.png"
    )

    # Duke criteria
    create_mnemonic_image(
        "Duke Criteria MAJOR",
        "BE PHAT",
        "B = Blood cultures (2x typical organisms)\nE = Echo evidence\nP = Prosthetic valve dehiscence\nH = HACEKs\nA = Abscess\nT = Typical bugs",
        "images/duke_criteria_mnemonic.png"
    )
