"""
CP1404 Practical
Sort files based on extension
"""
import os
import shutil


def main():
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('FilesToSort')
    existing_dirs = []

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            existing_dirs.append(filename)
            continue

        extension = filename.split('.')[1]
        if extension not in existing_dirs:
            try:
                os.mkdir(extension)
                existing_dirs.append(extension)
            except FileExistsError:
                print('File already exists')
        shutil.move(filename, extension + '/' + filename)

main()