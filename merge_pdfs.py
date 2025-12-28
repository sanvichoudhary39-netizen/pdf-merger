from PyPDF2 import PdfMerger
import os
import sys

pdf_folder =r"C:\Users\LENOVO\Desktop\pdfs"

output_file = "merged_output.pdf"

if not os.path.exists(pdf_folder):
    os.makedirs(pdf_folder)
    print(f"Folder '{pdf_folder}' created. Please add PDFs into this folder and rerun the script.")
    sys.exit()

print("Files in folder:", os.listdir(pdf_folder))  # Debug line

merger = PdfMerger()
pdf_count = 0

for file in sorted(os.listdir(pdf_folder)):
    if file.lower().endswith(".pdf"):
        full_path = os.path.join(pdf_folder, file)
        merger.append(full_path)
        print("Added:", file)
        pdf_count += 1

if pdf_count > 0:
    merger.write(output_file)
    merger.close()
    print(f"\nMerged {pdf_count} PDFs into '{output_file}'")
else:
    print("No PDFs found in the folder. Please add PDF files to merge.")

