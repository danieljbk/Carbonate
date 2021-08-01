import os
from shutil import rmtree as delete_directory
from path_management import get_filename_and_specific_directory, crawl


# delete carbon_copies made for Python files that no longer exist
def delete_obsolete_carbon_copies(carbon_copies_path=str, coding_folder_path=str):
    carbon_copies, python_files, remaining = [], [], []

    for filepath in crawl('.png', carbon_copies_path):
        filename, specific_directory = get_filename_and_specific_directory(
            '.png', filepath, carbon_copies_path)
        carbon_copies.append(specific_directory+'/'+filename)

    for filepath in crawl('.py', coding_folder_path):
        filename, specific_directory = get_filename_and_specific_directory(
            '.py', filepath, coding_folder_path)
        # because carbon files are saved with spaces converted to underscores
        filename = filename.replace(' ', '_')
        python_files.append(specific_directory+'/'+filename)

    for x in range(len(carbon_copies)):
        for y in range(len(python_files)):
            if carbon_copies[x] == python_files[y]:
                carbon_copies[x] = 0
                python_files[y] = 0
                break

    for x in range(len(carbon_copies)):
        if carbon_copies[x] != 0:
            remaining.append(carbon_copies[x])

    for x in remaining:
        os.remove(carbon_copies_path + x + '.png')


def delete_temporary_carbon_copies(carbon_copies_path=str):
    delete_directory(carbon_copies_path)
