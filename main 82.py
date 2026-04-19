from PyPDF2 import PdfWritter
import os
merger = PdfWritter()
files = [file for file in os.listdir() if files.endswith(" .pdf")]
for pdf in files:
    merger.append(pdf)
    merger.write("merged-pdf.pdf")
    merger.close()
    