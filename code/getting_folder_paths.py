from pathlib import Path


def get_user_input_folder_path(description):
    folder_path = input(
        f"Drag and drop the folder {description} into the Terminal.\n"
    ).strip()

    # replace '\' because Terminal adds the backslash character before spacing when retrieving file paths
    folder_path = folder_path.replace("\\", "")

    return folder_path


def get_user_general_downloads_path():
    # generic Mac download path should be: /Users/daniel/Downloads
    downloads_path = str(Path.home() / "Downloads")
    downloads_path += "/Carbon_Copies"

    return downloads_path


def set_folder_paths():
    coding_folder_path = get_user_input_folder_path("that contains your code files")
    temporary_carbon_copies_path = get_user_general_downloads_path()
    relocation_path = get_user_input_folder_path(
        "where you want to save the Carbon Copies to"
    )

    return coding_folder_path, temporary_carbon_copies_path, relocation_path
