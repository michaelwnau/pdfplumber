import csv
import pdfplumber

# Open the PDF file
with pdfplumber.open("zcg-pdf\2305-0639-zcg-capability-statement-b-w-v-2.pdf") as pdf:
    # Open the CSV file
    with open("my_csv.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        # Process each page in the PDF file
        for page in pdf.pages:
            # Extract the text from the page
            text = page.extract_text()
            # Write the text to the CSV file
            writer.writerow([text])
