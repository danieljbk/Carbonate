from path_management import absolute_path


def get_languages():
    f = open(absolute_path(".txt/code_file_extensions.txt"), 'r')
    languages = [x.rstrip() for x in f]  # remove line breaks
    f.close()

    return languages
