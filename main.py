from PyPDF2 import PdfMerger
import os

def find_files (pdfs=None):
    if pdfs is None:
        pdfs = []

    directory = os.path('C:\Users\Rick\Desktop')
    files = os.listdir()
    for f in files:
        if f.endswith('.pdf'):
            pdfs.append(f)


