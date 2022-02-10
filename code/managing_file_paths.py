import os
import glob


# input relative path, output absolute path
def absolute_path(path):
    dirname = os.path.dirname(__file__)

    return os.path.join(dirname, path)


# read code file and try to make it bash-compatible
def retrieve_code_from(filepath):
    f = open(filepath, "r")
    code = f.read()
    f.close()

    return code


# list all files using the glob module
def crawl(filetype=str, path=str):
    all_contents = glob.glob(path + "/**/*" + filetype, recursive=True)

    # I wanted to create carbon copies beginning at the highest level.
    # with this sort, the deepest folder (or really, the folder with the longest name) runs last
    all_contents.sort(key=len)

    return all_contents


def get_filename_and_specific_directory(filetype=str, filepath=str, folder_path=str):
    filename = ''.join(list(filepath[int(
        '-'+str(list(reversed(list(filepath))).index('/'))):])[:-len(filetype)])
    specific_directory = ''.join(list(filepath)[len(
        list(folder_path)):-len(filename)-len(filetype)-1]).replace(' ', '_')

    return filename, specific_directory
