#! /usr/bin/python

import os

def create_index(dirpath: str):
    os.chdir(dirpath)
    with open('index.md', "w") as f:
        for filename in sorted(os.listdir('.')):
            if os.path.isdir(filename):
                if filename.startswith('.') or filename == 'img':
                    continue
                f.write('+ [%s](%s/index.md)' % (filename, filename) + os.linesep)
                create_index(filename)
            else:
                if not filename.endswith('.md') or filename == 'index.md':
                    continue
                f.write('+ [%s](%s)' % (filename, filename) + os.linesep)
    os.chdir('..')

create_index('.')
