from get_folder_path import set_folder_paths
from creating import create_carbon_copies
from deleting import delete_obsolete_carbon_copies, delete_temporary_carbon_copies
from copying import copy_all_carbon_copies

# set the folder paths
coding_folder_path, temporary_carbon_copies_path, relocation_path = set_folder_paths()

# create the carbon copies
create_carbon_copies(coding_folder_path, temporary_carbon_copies_path)

# compare folders and delete any carbon copies for code files that don't exist anymore
delete_obsolete_carbon_copies(temporary_carbon_copies_path, coding_folder_path)

# once we have a nice set of carbon copies, relocate them to the desired user folder instead of the temporary location of 'downloads'
copy_all_carbon_copies(temporary_carbon_copies_path, relocation_path)

# then finally, delete the temporary files from the computer.
delete_temporary_carbon_copies(
    temporary_carbon_copies_path)
