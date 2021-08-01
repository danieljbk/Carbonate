from get_folder_path import get_user_input_folder_path, get_user_general_downloads_path
from get_languages import get_languages
from creating import create_carbon_copies_for_language
from deleting import delete_obsolete_carbon_copies, delete_temporary_carbon_copies
from copying import copy_all_carbon_copies


# set the folder paths
coding_folder_path = get_user_input_folder_path(
    "that contains your code files")
temporary_carbon_copies_path = get_user_general_downloads_path()
relocation_path = get_user_input_folder_path(
    "where you want to save the Carbon Copies to")

# create the carbon copies
for language in get_languages():  # for each language
    create_carbon_copies_for_language(
        language, coding_folder_path, temporary_carbon_copies_path)

# compare folders and delete any carbon copies for code files that don't exist anymore
delete_obsolete_carbon_copies(temporary_carbon_copies_path, coding_folder_path)

# once we have a nice set of carbon copies, relocate them to the desired user folder instead of the temporary location of 'downloads'
copy_all_carbon_copies(temporary_carbon_copies_path, relocation_path)

# then finally, delete the temporary files from the computer.
delete_temporary_carbon_copies(
    temporary_carbon_copies_path)
