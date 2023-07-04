import csv
import pdfplumber

# Specify the full paths to your output files
txt_file_path = "/full/path/to/my_txt.txt"
csv_file_path = "/full/path/to/my_csv.csv"

# Open the PDF file
with pdfplumber.open("zcg-pdf\\2305-0639-zcg-capability-statement-b-w-v-2.pdf") as pdf:
    # Open the txt file
    with open(txt_file_path, "w") as txt_file:
        # Open the CSV file
        with open(csv_file_path, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            # Process each page in the PDF file
            for page in pdf.pages:
                # Extract the text from the page
                text = page.extract_text()
                # Write the text to the txt file
                txt_file.write(text + "\n")
                # Write the text to the CSV file
                writer.writerow([text])
