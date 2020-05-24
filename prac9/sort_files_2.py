"""
CP1404 Practical
Sort files based on extension and user categorisation
"""
import os
import shutil


def main():
    input_category_list = {'Docs' : ['doc', 'docx', 'txt'], 'Images' : ['png', 'gif', 'jpg'],
                           'Spreadsheets' : ['xls', 'xlsx'], 'text' : []}
    print(input_category_list)
    os.chdir("FilesToSort")
    existing_dirs = []
    for folder_name in input_category_list.keys():
        try:
            os.mkdir(folder_name)
        except FileExistsError:
            print('Folder {} already exists'.format(folder_name))
    for key, extension_list in input_category_list.items():
        pass
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        for folder_name, extension_list in input_category_list.items():
            extension = filename.split('.')[1]
            if extension in extension_list :
                shutil.move(filename, folder_name + '/' + filename)

main()