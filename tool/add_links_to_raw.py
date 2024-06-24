#!/usr/bin/env python3

import os

def add_link_to_html_body():
    for root, dirs, files in os.walk("export_xhtml"):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                # count number of slashes in file path
                slashes = file_path.count("/") + file_path.count("\\")
                link = "../" * slashes + file_path.replace("\\", "/").replace("export_xhtml/", "export_raw/").replace(".html", ".txt")
                with open(file_path, "r+", encoding="utf-8") as f:
                    content = f.read()
                    f.seek(0)
                    f.write(content.replace("<body>", f"<body><a href='{link}'>Wikiマークアップ</a><br>"))
                    f.truncate()

if __name__ == "__main__":
    add_link_to_html_body()
