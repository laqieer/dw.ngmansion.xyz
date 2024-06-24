#!/usr/bin/env python3

import os
from bs4 import BeautifulSoup

folder_path = 'wiki'

# Loop through all files in the folder
for root, dirs, filenames in os.walk(folder_path):
    for filename in filenames:
        if filename.endswith('.html'):
            file_path = os.path.join(root, filename)

            # Read the file content
            with open(file_path, 'r', encoding="utf-8") as file:
                html = file.read()

            # Parse the HTML using BeautifulSoup
            soup = BeautifulSoup(html, 'html.parser')

            # Remove all link tags and script tags in head part
            head = soup.find('head')
            if head:
                if not head.find('link'):
                    continue
                for link in head.find_all('link'):
                    link.decompose()
                for script in head.find_all('script'):
                    script.decompose()

            # Find and remove the div with id 'dokuwiki__header'
            div_header = soup.find('div', id='dokuwiki__header')
            if div_header:
                div_header.decompose()

            # Find and remove the div with id 'dokuwiki__footer'
            div_footer = soup.find('div', id='dokuwiki__footer')
            if div_footer:
                div_footer.decompose()

            # Find and remove the div with id 'dokuwiki__aside'
            div_aside = soup.find('div', id='dokuwiki__aside')
            if div_aside:
                div_aside.decompose()

            # Find and remove the div with id 'dokuwiki__pagetools'
            div_pagetools = soup.find('div', id='dokuwiki__pagetools')
            if div_pagetools:
                div_pagetools.decompose()

            # Find and remove the div with class 'addnewpage'
            div_addnewpage = soup.find('div', class_='addnewpage')
            if div_addnewpage:
                div_addnewpage.decompose()

            # Find and remove all form tags
            for form in soup.find_all('form'):
                form.decompose()

            # Add link to exported_xhtml and exported_raw to the top of the body
            body = soup.find('body')
            if body:
                slashes = file_path.count("/") + file_path.count("\\")
                link_base = "../" * slashes
                fn = file_path.replace("\\", "/").replace("wiki/", "export_xhtml/")
                if os.path.exists(fn):
                    link = link_base + fn
                    a = soup.new_tag('a', href=link)
                    a.string = 'プレーンHTML'
                    body.insert(0, a)
                    body.insert(1, ' | ')
                    link = link.replace("export_xhtml/", "export_raw/").replace(".html", ".txt")
                    a = soup.new_tag('a', href=link)
                    a.string = 'Wikiマークアップ'
                    body.insert(2, a)
                    # Add a line break
                    body.insert(3, soup.new_tag('br'))

            # Save the modified HTML back to the file
            with open(file_path, 'w', encoding="utf-8") as file:
                file.write(str(soup))
