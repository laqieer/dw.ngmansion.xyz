#!/usr/bin/env python3

import os
import sys

def rename_files(folder_path, file_ext):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if not file_path.endswith(file_ext) and os.path.isfile(file_path):
            s = filename.split(r'%26id%3d')[-1]
            new_name = '.' + file_ext
            if s.strip() == '':
                new_name = 'index' + new_name
            else:
                new_name = s.replace(r'%3a', '\\') + new_name
            new_file_path = os.path.join(folder_path, new_name)
            if not os.path.exists(os.path.dirname(new_file_path)):
                os.makedirs(os.path.dirname(new_file_path))
            os.rename(file_path, new_file_path)

if __name__ == '__main__':
    rename_files(sys.argv[1], sys.argv[2])
