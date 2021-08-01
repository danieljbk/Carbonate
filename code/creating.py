import os

from path_management import absolute_path, crawl, get_filename_and_specific_directory, retrieve_code_from


def create_carbon_copies_for_language(language=str, coding_folder_path=str, carbon_copies_path=str):
    for filepath in crawl(language, coding_folder_path):
        filename, specific_directory = get_filename_and_specific_directory(
            language, filepath, coding_folder_path)
        convert_to_bash_and_run(retrieve_code_from(
            filepath), filename.replace(' ', '_'), specific_directory, carbon_copies_path)


def convert_to_bash_and_run(code=str, python_file_name=str, specific_directory=str, carbon_copies_path=str):
    if not os.path.exists(carbon_copies_path + specific_directory):
        os.makedirs(carbon_copies_path + specific_directory)

    png_file_name = carbon_copies_path + \
        specific_directory + f"/{python_file_name}.png"

    f = open(png_file_name, 'w')
    f.close()

    # read json data from json file
    f = open(absolute_path(".json/carbon-config.json"), 'r')
    json = f.readline().strip()
    json = json[1:-1]  # get rid of brackets
    f.close()

    # script to run in Terminal to create Carbon Copy
    bash_script = f"""
    curl -L https://carbonara.vercel.app/api/cook \\
    -X POST \\
    -H 'Content-Type: application/json' \\
    -d '{{
        "code": "{code}",
        {json}
        }}' \\
    > {png_file_name}
    """

    print(png_file_name)
    os.system(bash_script)  # run
    print()
    print()
