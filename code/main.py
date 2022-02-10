from getting_folder_paths import set_folder_paths
from creating import create_carbon_copies
from deleting import delete_obsolete_carbon_copies, delete_temporary_carbon_copies
from copying import copy_all_carbon_copies

# 1. set the folder paths
coding_folder_path, temporary_carbon_copies_path, relocation_path = set_folder_paths()

# 2. create the carbon copies
create_carbon_copies(coding_folder_path, temporary_carbon_copies_path)

# 3. compare folders and delete any carbon copies for code files that don't exist anymore
delete_obsolete_carbon_copies(temporary_carbon_copies_path, coding_folder_path)

# 4. once we have a nice set of carbon copies, relocate them to the desired user folder instead of the temporary location of 'downloads'
copy_all_carbon_copies(temporary_carbon_copies_path, relocation_path)

# 5. then finally, delete the temporary files from the computer.
delete_temporary_carbon_copies(temporary_carbon_copies_path)
