import os
import csv
from docx import Document


def process_docx(docx_file):
    # Get the base name of the Word file (without the extension)
    base_name = os.path.splitext(os.path.basename(docx_file))[0]

    # Specify the paths to your output files
    txt_file_path = f"{base_name}.txt"
    csv_file_path = f"{base_name}.csv"

    # Open the Word file
    doc = Document(docx_file)

    # Open the txt file
    with open(txt_file_path, "w", encoding="utf-8") as txt_file:
        # Open the CSV file
        with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            # Process each paragraph in the Word file
            for para in doc.paragraphs:
                # Extract the text from the paragraph
                text = para.text
                # If text is not None, write it to the files
                if text is not None:
                    # Write the text to the txt file
                    txt_file.write(text + "\n")
                    # Write the text to the CSV file
                    writer.writerow([text])

    print(f"Done processing {docx_file}!")


# Now you can call process_docx with the path to a Word file
process_docx(
    r"C:\Users\micha\OneDrive\Desktop\pdfplumber\pdfplumber\word-process\Common EVSS Developer Setup.docx"
)
