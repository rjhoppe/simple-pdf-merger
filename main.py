from PyPDF2 import PdfWriter
import os
import sys
import shutil

def find_files (pdfs=None):
    if pdfs is None:
        pdfs = []

    directory = (os.environ['USERPROFILE'] + '\Desktop')
    files = os.listdir(directory)
    for f in files:
        if f.endswith('.pdf'):
            pdfs.append(f)
    return pdfs

pdfs = find_files()

def return_files (pdfs):
    print('These are your PDF files available to merge:')
    print(pdfs)

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
        elif merge_file1 == 'Exit' or merge_file1 == 'exit':
            sys.exit()
        else:
            print("This file does not exist. Please make sure the file name is spelled correctly and it is located on your desktop.")
            return select_file_one ()
    
    select_file_one ()

    def select_file_two (func_iterator=2, add_marker = False):
        print(f"File #{func_iterator}:")
        merge_file2 = input()
        if merge_file2 in pdfs:
            pdfs_selected.append(merge_file2)
            print("Do you have any more files to merge? Y/N")
            answer = input()
            if answer == 'Y' or answer == 'y':
                print(f'Files selected: {pdfs_selected}')
                func_iterator+=1
                return select_file_two (func_iterator)
            if answer == 'N' or answer == 'n':
                print(f'Files selected: {pdfs_selected}')
                # Added logic to handle when a user adds / deletes files
                if add_marker is True:
                    merger = PdfWriter()
                    pdf_path = {}
                    for p in pdfs_selected:
                        full_path = (os.environ['USERPROFILE'] + '\Desktop' + '\\' + p)
                        pdf_path.update({p: full_path})

                    for key, value in pdf_path.items():
                        source = value
                        dest = (os.environ['USERPROFILE'] + '\Documents\Python_Practice\Simple PDF Merger' + '\\' + key)
                        shutil.copyfile(source, dest)

                    for pdf in pdfs_selected:
                        merger.append(pdf)

                    merger.write("merged-file.pdf")
                    merger.close()
                    print('Job done.')
                   
            else:
                print("Command not recognized.")
        elif merge_file2 == 'Exit' or merge_file2 == 'exit':
            sys.exit()
        else:
            print("This file does not exist. Please make sure the file name is spelled correctly and it is located on your desktop.")
            return select_file_two (func_iterator)
            
    select_file_two ()
            
    # Merge files must be unique - i.e. cannot merge the same file
    def merge_files (pdfs_selected, pdf_path=None):
        if pdf_path is None:
            pdf_path = {}

        print(f'Prepping the following files for merging: {pdfs_selected}')
        print("Finalize this merge? Y/N")
        finalize = input()
        if finalize == 'Y' or finalize == 'y':

            merger = PdfWriter()
            for p in pdfs_selected:
                full_path = (os.environ['USERPROFILE'] + '\Desktop' + '\\' + p)
                pdf_path.update({p: full_path})

            for key, value in pdf_path.items():
                source = value
                dest = (os.environ['USERPROFILE'] + '\Documents\Python_Practice\Simple PDF Merger' + '\\' + key)
                shutil.copyfile(source, dest)

            for pdf in pdfs_selected:
                merger.append(pdf)

            merger.write("merged-file.pdf")
            merger.close()
            print('Job done.')
        
        elif finalize == 'N' or finalize == 'n':
            print('What action would you like to take: Add, Delete, Exit')
            action = input()
            if action == 'Add' or action == 'add':
                return select_file_two(func_iterator=(len(pdfs_selected)+1), add_marker=True)

            elif action == 'Delete' or action == 'delete':
                print('Which file would you like to delete from your list?')
                print(pdfs_selected)
                delete_choice = input()
                if delete_choice in pdfs_selected:
                    pdfs_selected.remove(delete_choice)
                    return merge_files (pdfs_selected)

            elif action == 'Exit' or action == 'exit':
                sys.exit()

            else:
                print('Command not recognized, please try again.')
                return merge_files()

        elif finalize == 'Exit' or finalize == 'exit':
            sys.exit()

        else:
            print('Command not recognized, please try again.')
            return merge_files()

    merge_files (pdfs_selected)

select_files(pdfs)

def clean_up_dir ():

    cwd = os.listdir()
    for file in cwd:
        if file.endswith('.pdf') and file != 'merged-file.pdf':
            os.remove(file)

    source = 'C:/Users/Rick/Documents/Python_Practice/Simple PDF Merger/merged-file.pdf'
    dest = 'C:/Users/Rick/Desktop\merged-file.pdf'
    shutil.copyfile(source, dest)
    os.remove('merged-file.pdf')
    print('Directories cleaned up. Please find your new file on your desktop!')
    
clean_up_dir ()
