import os
import glob
from code_editing import replace_problematic_characters


def absolute_path(path):  # input relative path, output absolute path
    dirname = os.path.dirname(__file__)

    return os.path.join(dirname, path)


# read code file and try to make it bash-compatible
def retrieve_code_from(filepath):
    f = open(filepath, "r")
    code = f.read()
    f.close()

    code = replace_problematic_characters(code)

    return code


def crawl(filetype=str, path=str):  # list all files using the glob module
    all_contents = glob.glob(path + "/**/*" + filetype, recursive=True)

    # downward from top level. deepest folder runs last (generally)
    all_contents.sort(key=len)

    return all_contents


def get_filename_and_specific_directory(filetype=str, filepath=str, folder_path=str):
    filename = ''.join(list(filepath[int(
        '-'+str(list(reversed(list(filepath))).index('/'))):])[:-len(filetype)])
    specific_directory = ''.join(list(filepath)[len(
        list(folder_path)):-len(filename)-len(filetype)-1]).replace(' ', '_')

    return filename, specific_directory
