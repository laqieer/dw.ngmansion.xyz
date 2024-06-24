#!/usr/bin/env python3

import os

def build_index():
    # Directory containing the HTML files
    html_dir = 'export_xhtml'

    # List to store the files
    files = []

    # Scan the directory for HTML files
    for root, dirs, filenames in os.walk(html_dir):
        for filename in filenames:
            if filename.endswith('.html'):
                files.append(os.path.relpath(os.path.join(root, filename), html_dir).replace('\\', '/'))

    # Sort the files alphabetically
    files.sort()

    # Create the index.html file
    with open('index.html', 'w', encoding="utf-8") as index_file:
        index_file.write('<html>\n')
        index_file.write('<head>\n')
        index_file.write('<title>FE改造wiki</title>\n')
        index_file.write('</head>\n')
        index_file.write('<body>\n')
        index_file.write('<h1>Index of HTML Files</h1>\n')
        index_file.write('<ul>\n')

        # Write the links to the index.html file
        for file in files:
            link = f'<li><a href="{html_dir}/{file}">{file}</a></li>\n'
            index_file.write(link)

        index_file.write('</ul>\n')
        index_file.write('</body>\n')
        index_file.write('</html>\n')

    print('Index.html file created successfully.')

if __name__ == '__main__':
    # Call the function to build the index.html file
    build_index()
