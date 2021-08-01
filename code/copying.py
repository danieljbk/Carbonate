import os
from shutil import copyfile
from managing_file_paths import crawl, get_filename_and_specific_directory


# copies all contents to folder in /Daniel's Files
def copy_all_carbon_copies(original_path=str, relocation_path=str):
    relocation_path += "/Carbon_Copies"
    for filepath in crawl('.png', original_path):
        filename, specific_directory = get_filename_and_specific_directory(
            '.png', filepath, original_path)

        newpath = relocation_path + specific_directory
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        if filename:
            copyfile(filepath, newpath + '/' + filename + '.png')
