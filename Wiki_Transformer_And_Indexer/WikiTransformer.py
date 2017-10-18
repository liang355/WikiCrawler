import os
import re


def run_transformer(folder_name, num_files_to_process):
    for filename in os.listdir(folder_name)[:num_files_to_process]:
        with open(folder_name + '/' + filename, 'r') as f:
            page = f.read()

