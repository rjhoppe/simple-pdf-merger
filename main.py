from PyPDF2 import PdfMerger
import os
import sys

def find_files (pdfs=None):
    if pdfs is None:
        pdfs = []

    directory = (os.environ['USERPROFILE'] + '\Desktop')
    files = os.listdir(directory)
    # print(files)
    for f in files:
        if f.endswith('.pdf'):
            pdfs.append(f)
    return pdfs

pdfs = find_files()
print(pdfs)

def return_files (pdfs):
    print('These are your PDF files available to merge:')
    for f in pdfs:
        print(f)

return_files (pdfs)

def select_files(pdfs, pdfs_selected=None):
    print('Test')
    if pdfs_selected is None:
        pdfs_selected = []

    def select_file_one ():
        print('Please select at least two files to merge')
        print("File #1:")
        merge_file1 = input()
        if merge_file1 in pdfs:
            pdfs_selected.append(select_file_one)
        elif merge_file1 == 'Exit':
            sys.exit()
        else:
            print("This file does not exist. Please make sure the file name is spelled correctly and it is located on your desktop.")
            return select_file_one ()
    
    select_file_one ()

    def select_file_two (func_iterator=2):
        print(f"File #{func_iterator}:")
        merge_file2 = input()
        if merge_file2 in pdfs:
            pdfs_selected.append(select_file_one)
            print("Do you have any more files to merge? Y/N")
            answer = input()
            if answer == 'Y' or 'y':
                func_iterator+=1
                return select_file_two (func_iterator)
        elif merge_file2 == 'Exit' or 'exit':
            sys.exit()
        elif merge_file2 == 'N' or 'n':
            pass
        else:
            print("This file does not exist. Please make sure the file name is spelled correctly and it is located on your desktop.")
            return select_file_two ()
            
    select_file_two ()
            
    def merge_files (pdfs_selected):
        merger = PdfMerger()

        for p in pdfs_selected:
            merger.append(p)

        merger.write("mergedfile.pdf")
        merger.close()
        print('Job done.')

    merge_files (pdfs_selected)

select_files(pdfs)

