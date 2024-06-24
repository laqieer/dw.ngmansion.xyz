#!/usr/bin/env python3

import os

def rename_files():
    for filename in os.listdir('media'):
        file_path = os.path.join('media', filename)
        if os.path.isfile(file_path):
            s = filename.split(r'media%3d')[-1]
            new_name = s.replace(r'%3a', '\\')
            new_file_path = os.path.join('wiki_pages', new_name)
            if os.path.exists(new_file_path):
                continue
            if not os.path.exists(os.path.dirname(new_file_path)):
                os.makedirs(os.path.dirname(new_file_path))
            os.rename(file_path, new_file_path)

if __name__ == '__main__':
    rename_files()
