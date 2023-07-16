import glob
from fpdf import FPDF
from pathlib import Path

# Create a list of text filepaths
filepaths = glob.glob("Text+Files/*.txt")
# Create one PDF file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Gp through each text file
for filepath in filepaths:
    # Add a page to the PDF document for each text file
    pdf.add_page()

    # Get the filename without the extension
    # add convert it to title case (e.g. Cat)
    filename = Path(filepath).stem
    name = filename.title()

    # Add the name to the PDF
    pdf.set_font(family="times", size=16, style="B")
    pdf.cell(w=58, h=8, txt=name, ln=1)

    # Get the content of each text file
    with open(filepath, "r") as file:
        content = file.read()
    # Add the text file content to the PDF
    pdf.set_font(family="Times", size=10)
    pdf.multi_cell(w=0, h=6, txt=content)

# Produce the PDF
pdf.output("output.pdf")