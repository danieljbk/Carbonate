from pathlib import Path


def get_user_input_folder_path(description):
    folder_path = input(
        f"Drag and drop the folder {description} into the Terminal.\n").strip()
    # replace '\' because Terminal adds the backslash character before spacing when retrieving file paths
    folder_path = folder_path.replace('\\', '')

    return folder_path


def get_user_general_downloads_path():
    # generic Mac download path should be: /Users/daniel/Downloads
    downloads_path = str(Path.home() / "Downloads")
    downloads_path += '/Carbon_Copies'
    print(downloads_path)
    return downloads_path
