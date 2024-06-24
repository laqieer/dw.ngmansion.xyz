#!/usr/bin/env python3

import os
import sys
from bs4 import BeautifulSoup

def fix_urls_in_html_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    html_content = f.read()
                soup = BeautifulSoup(html_content, "html.parser")
                for link in soup.find_all("a"):
                    if link.has_attr("href"):
                        old_url = link["href"]
                        # Perform URL fixing logic here
                        new_url = fix_url(folder_path, file_path, old_url)
                        link["href"] = new_url
                for link in soup.find_all("img"):
                    if link.has_attr("src"):
                        old_url = link["src"]
                        # Perform URL fixing logic here
                        new_url = fix_url(folder_path, file_path, old_url)
                        link["src"] = new_url
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(str(soup))

def decode_url(url):
    # Implement your URL decoding logic here
    # For example, you can use regular expressions or string manipulation functions
    # to decode the URL as needed
    # Return the decoded URL
    url = url.replace(r"%3A", ":").replace(r"%2F", "/").replace(r"%3F", "?").replace(r"%3D", "=")
    return url

def calculate_relative_path(file_path, url):
    # Implement your relative path calculation logic here
    # For example, you can use string manipulation functions to calculate the relative path
    # between the file and the URL
    # Return the relative path
    file_path = file_path.replace("\\", "/").replace("./", "").split("/")
    url = url.replace("\\", "/").split("/")
    i = 0
    while i < len(file_path) and i < len(url) and file_path[i] == url[i]:
        i += 1
    relative_path = [".."] * (len(file_path) - i - 1) + url[i:]
    return "/".join(relative_path)

def fix_url(folder_path, file_path, url):
    # Implement your URL fixing logic here
    # For example, you can use regular expressions or string manipulation functions
    # to modify the URL as needed
    # Return the fixed URL
    if url.startswith("/doku.php?"):
        if "idx" in url:
            # extract folder name
            url = url.split("idx=")[-1]
            # link to index.html in folder
            url = decode_url(url).replace(":", "/") + "/index.html"
            url = calculate_relative_path(file_path, os.path.join(folder_path, url))
            return url
        if "id" in url:
            # extract page name
            url = url.split("id=")[-1]
            # link to page in the same wiki
            url = decode_url(url).replace(":", "/") + ".html"
            url = calculate_relative_path(file_path, os.path.join(folder_path, url))
            return url
    if url.startswith("/lib/exe/"):
        # extract media URL
        url = url.split("media=")[-1]
        # decode special characters in URL
        url = decode_url(url)
        return url
    return url

if __name__ == "__main__":
    fix_urls_in_html_files(sys.argv[1])
