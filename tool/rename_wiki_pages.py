#!/usr/bin/env python3

import os
from urllib.parse import unquote

def rename_files(folder_path, file_ext):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if not filename.endswith(file_ext):
            continue
        decoded_filename = unquote(filename)
        if '&' in decoded_filename:
            os.remove(file_path)
            continue
        if os.path.isfile(file_path):
            new_name = decoded_filename.split('?id=')[-1].replace(':', '\\')
            if new_name.endswith('\\.' + file_ext):
                new_name.replace('\\.' + file_ext, '\\index.' + file_ext)
            new_file_path = os.path.join(folder_path, new_name)
            if not os.path.exists(os.path.dirname(new_file_path)):
                os.makedirs(os.path.dirname(new_file_path))
            os.rename(file_path, new_file_path)

if __name__ == '__main__':
    rename_files('wiki_pages', 'html')
