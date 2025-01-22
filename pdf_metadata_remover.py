import pikepdf

file_path = r"C:\Users\dinko\Desktop\.pdf"

# Open the PDF file
pdf = pikepdf.open(file_path)

# Remove all metadata from the PDF
pdf.metadata = {}

# Access the docinfo dictionary (which holds metadata like Creator and Producer)
info = pdf.docinfo

# Remove the 'Creator' and 'Producer' fields using del
if '/Creator' in info:
    del info['/Creator']
if '/Producer' in info:
    del info['/Producer']

# Save the modified PDF to a new file
output_path = r"C:\Users\dinko\Desktop\_no_metadata.pdf"
pdf.save(output_path)

