import os
import json
import requests
from getting_coding_languages import get_languages
from managing_file_paths import absolute_path, crawl, get_filename_and_specific_directory, retrieve_code_from


def create_for_each_language(language=str, coding_folder_path=str, carbon_copies_path=str):
    for filepath in crawl(language, coding_folder_path):
        filename, specific_directory = get_filename_and_specific_directory(
            language, filepath, coding_folder_path)
        convert_to_bash_and_run(retrieve_code_from(
            filepath), filename.replace(' ', '_'), specific_directory, carbon_copies_path)


def create_carbon_copies(coding_folder_path, temporary_carbon_copies_path):
    for language in get_languages():  # for each language
        create_for_each_language(
            language, coding_folder_path, temporary_carbon_copies_path)


def convert_to_bash_and_run(code=str, python_file_name=str, specific_directory=str, carbon_copies_path=str):
    if not os.path.exists(carbon_copies_path + specific_directory):
        os.makedirs(carbon_copies_path + specific_directory)

    png_file_name = carbon_copies_path + \
        specific_directory + f"/{python_file_name}.png"

    # read json data from json file
    f = open(absolute_path(".json/carbon-config.json"), 'r')
    jayson = f.readline().strip()
    jayson = json.loads(jayson)
    f.close()

    data = {}
    data["code"] = code
    data.update(jayson)

    r = requests.post(
        url="https://carbonara-42.herokuapp.com/api/cook", json=data)

    print("SUCCESS:", png_file_name)

    with open(png_file_name, "wb") as f:
        f.write(r.content)
