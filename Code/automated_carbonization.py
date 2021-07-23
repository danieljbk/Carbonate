import os
import glob
from shutil import copyfile


def retrieve_code_from(filepath): # read code file and try to make it bash-compatible
    f = open(filepath, "r")
    code = f.read()
    f.close()
    
    code = list(code)
    while '"' in code:
        for i in range(len(code)):
            if code[i] == '"':
                code[i] = '“'
                break
        for i in range(len(code)):
            if code[i] == '"':
                code[i] = '”'
                break
    
    # convert problematic characters to lookalike unicode characters: https://unicode-table.com/en/
    while "'" in code:
        for i in range(len(code)):
            if code[i] == "'":
                code[i] = "‘"
                break
        for i in range(len(code)):
            if code[i] == "'":
                code[i] = "’"
                break
    code = ''.join(code)

    code = code.replace('{', '❴')
    code = code.replace('}', '❵')
    code = code.replace('(', '❪')
    code = code.replace(')', '❫')
    code = code.replace(')', '❫')
    code = code.replace('/', '󠀠╱') # https://unicode-table.com/en/blocks/box-drawing/
    code = code.replace('\\n', '╲n') # https://unicode-table.com/en/blocks/box-drawing/, greek letter nu could be useful
    code = code.replace("\r", "\\r")
    code = code.replace("\n", "\\n")
    while list(code)[:2] == ['\\', 'n']:
        code = "".join(list(code)[2:])
    if list(code)[-2:] != ['\\', 'n', '\\', 'n',]:
        code += '\\n'
    
    return code


def convert_to_bash_and_run(code=str, python_file_name=str, specific_directory=str):
    carbon_copies_path = "/Users/daniel/Applications/Carbon_Copies"
    
    if not os.path.exists(carbon_copies_path + specific_directory):
        os.makedirs(carbon_copies_path + specific_directory)
    
    png_file_name = carbon_copies_path + specific_directory + f"/{python_file_name}.png"
    
    f = open(png_file_name, 'w')
    f.close()
    
    bash_script = f"""
    curl -L https://carbonara.vercel.app/api/cook \\
    -X POST \\
    -H 'Content-Type: application/json' \\
    -d '{{
        "code": "{code}",
        "paddingVertical":"56px","paddingHorizontal":"56px","backgroundImage":null,"backgroundImageSelection":null,"backgroundMode":"color","backgroundColor":"rgba(171, 184, 195, 1)","dropShadow":true,"dropShadowOffsetY":"20px","dropShadowBlurRadius":"68px","theme":"lucario","windowTheme":"none","language":"auto","fontFamily":"Hack","fontSize":"14px","lineHeight":"133%","windowControls":true,"widthAdjustment":true,"lineNumbers":false,"firstLineNumber":1,"exportSize":"4x","watermark":false,"squaredImage":false,"hiddenCharacters":false,"name":"","width":680
        }}' \\
    > {png_file_name}
    """
    
    print(png_file_name)
    os.system(bash_script)
    print()
    print()


def crawl(filetype=str, path=str): # list all files using the glob module
    all_contents = glob.glob(path + "/**/*" + filetype, recursive=True)
    all_contents.sort(key=len) # downward from top level. deepest folder runs last (generally)
    
    return all_contents


def get_filename_and_specific_directory(filetype=str, filepath=str, folder_path=str):
    filename = ''.join(list(filepath[int('-'+str(list(reversed(list(filepath))).index('/'))):])[:-len(filetype)])
    specific_directory = ''.join(list(filepath)[len(list(folder_path)):-len(filename)-len(filetype)-1]).replace(' ', '_')
    
    return filename, specific_directory


def clear_obsolete(carbon_copies_path=str, coding_folder_path=str): # delete carbon_copies made for Python files that no longer exist
    carbon_copies, python_files, remaining = [], [], []
    
    for filepath in crawl('.png', carbon_copies_path):
        filename, specific_directory = get_filename_and_specific_directory('.png', filepath, carbon_copies_path)
        carbon_copies.append(specific_directory+'/'+filename)
    
    for filepath in crawl('.py', coding_folder_path):
        filename, specific_directory = get_filename_and_specific_directory('.py', filepath, coding_folder_path)
        filename = filename.replace(' ', '_') # because carbon files are saved with spaces converted to underscores
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


def create_carbon_copies_for_language(language=str, coding_folder_path=str):
    for filepath in crawl(language, coding_folder_path):
        filename, specific_directory = get_filename_and_specific_directory(language, filepath, coding_folder_path)
        convert_to_bash_and_run(retrieve_code_from(filepath), filename.replace(' ', '_'), specific_directory)


def copy_all_carbon_copies(original_path=str, relocation_path=str): # copies all contents to folder in /Daniel's Files
    for filepath in crawl('.png', original_path):
        filename, specific_directory = get_filename_and_specific_directory('.png', filepath, original_path)
        
        newpath = relocation_path + specific_directory
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        
        if filename:
            copyfile(filepath, newpath + '/' + filename + '.png')


def run():
    carbon_copies_path = "/Users/daniel/Applications/Carbon_Copies"
    coding_folder_path = "/Users/daniel/Library/Mobile Documents/com~apple~CloudDocs/Daniel's Files/Coding"

    my_languages = ['.py', '.cpp', '.js', '.java']
    for language in my_languages:
        create_carbon_copies_for_language(language, coding_folder_path)

    clear_obsolete(carbon_copies_path, coding_folder_path)
    
    relocation_path = "/Users/daniel/Library/Mobile Documents/com~apple~CloudDocs/Daniel's Files/Coding – Carbon Copies"
    copy_all_carbon_copies(carbon_copies_path, relocation_path)


if __name__ == "__main__":
    run()
