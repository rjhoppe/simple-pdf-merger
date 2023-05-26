from PyPDF2 import PdfMerger
import os
import sys

def find_files (pdfs=None):
    if pdfs is None:
        pdfs = []

    directory = (os.environ['USERPROFILE'] + '\Desktop')
    files = os.listdir(directory)
    print(files)
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
            pdfs_selected.append(merge_file1)
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
            pdfs_selected.append(merge_file2)
            print("Do you have any more files to merge? Y/N")
            answer = input()
            if answer == 'Y':
                print(f'Files selected: {pdfs_selected}')
                func_iterator+=1
                return select_file_two (func_iterator)
            if answer == 'N':
                print(f'Files selected: {pdfs_selected}')
            else:
                print("Command not recognized.")
        elif merge_file2 == 'Exit':
            sys.exit()
        else:
            print("This file does not exist. Please make sure the file name is spelled correctly and it is located on your desktop.")
            return select_file_two (func_iterator)
            
    select_file_two ()
            
    def merge_files (pdfs_selected):
        print(f'Prepping the following files for merging: {pdfs_selected}')
        print("Finalize this merge? Y/N")
        finalize = input()
        if finalize == 'Y':
            merger = PdfMerger()

            for p in pdfs_selected:
                # p = os.environ['USERPROFILE'] + '\Desktop' + p
                # Need to copy files to this directory
                # What to do with duplicates? - Only allow one of each
                # Copy files to pdf_files folder, merge files, delete copied files, push copied filed to desktop, delete merged copy
                merger.append(p)

            merger.write("mergedfile.pdf")
            merger.close()
            print('Job done.')
        
        elif finalize == 'N':
            print('What action would you like to take: Add, Delete, Exit')
            action = input()
            if action == 'Add': 
                return select_file_two(func_iterator=(len(pdfs_selected)+1))

            elif action == 'Delete':
                print('Which file would you like to delete from your list?')
                print(pdfs_selected)
                delete_choice = input()
                if delete_choice in pdfs_selected:
                    pdfs_selected.remove(delete_choice)
                    return merge_files (pdfs_selected)

            elif action == 'Exit':
                sys.exit()

            else:
                print('Command not recognized, please try again.')
                return merge_files()

        elif finalize == 'Exit':
            sys.exit()

        else:
            print('Command not recognized, please try again.')
            return merge_files()

    merge_files (pdfs_selected)

select_files(pdfs)

