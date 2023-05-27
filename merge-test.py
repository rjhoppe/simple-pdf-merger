from PyPDF2 import PdfWriter, PdfFileMerger
import os
from pathlib import Path
merger = PdfWriter()

list = ["C:\\Users\\Rick\\Documents\\Python_Practice\\Simple PDF Merger\\simple-pdf-merger\\PDF_Test_1.pdf", "C:\\Users\\Rick\\Documents\\Python_Practice\\Simple PDF Merger\\simple-pdf-merger\\PDF_Test_2.pdf"]
# list2 = ['PDF_Test_1.pdf', 'PDF_Test_2.pdf']

# path = "C:\\Users\\Rick\\Desktop\\Documents\\Python_Practice\\Simple PDF Merger\\simple-pdf-merger"
# os.chdir(path)

print(os.listdir())

# directory =
# file =
# open(os.path.join(directory, file), "r")

new_paths = []

pdf1_path = Path.cwd() / 'PDF_Test_1.pdf'
new_paths.append(pdf1_path)
pdf2_path = Path.cwd() / 'PDF_Test_2.pdf'
new_paths.append(pdf2_path)
print(new_paths)


# ospath = os.getcwd()
# print(ospath)


# file_list = ["PDF_Test_1.pdf", "PDF_Test_2.pdf"]
# abs_file_list = []

# path = os.getcwd

cwd = os.listdir()
dir_list = []
for c in cwd:
    dir_list.append(c)
print(dir_list)
dir_pdf_list = ['PDF_Test _1.pdf', 'PDF_Test_2.pdf']


for pdf in dir_pdf_list:
    merger.append(pdf)


#     path = "C:\\Users\\Rick\\Desktop\\Documents\\Python_Practice\\Simple PDF Merger\\simple-pdf-merger"
#     os.chdir(path)

merger.write("merged-pdf.pdf")
merger.close()