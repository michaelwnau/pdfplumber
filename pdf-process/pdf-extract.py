import os
import pdfplumber

# Ask the user for the PDF file location
pdf_file = input("Please enter the path to the PDF file: ")

# Open the PDF file
with pdfplumber.open(pdf_file) as pdf:
    # Extract the text from the first page
    first_page = pdf.pages[0]
    text = first_page.extract_text()

    # Replace line breaks with spaces and convert to lowercase
    text = text.replace("\n", " ").lower()

    # Get the base name of the PDF file (without the extension)
    base_name = os.path.splitext(pdf_file)[0]

    # Open the txt file and write the text to it
    with open(f"{base_name}.txt", "w") as txt_file:
        txt_file.write(text)

print("Done!")
