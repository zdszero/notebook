#! /usr/bin/python

import os

OUTPUT_FILE = open('./index.md', 'w')

def walk_dir(rel_path: str, dep: int):
    for file_name in os.listdir(rel_path):
        file_path = rel_path + '/' + file_name
        if not file_name.startswith('.') and file_name != 'img' and os.path.isdir(file_path):
            OUTPUT_FILE.write('{} [{}]({})'.format('#' * dep, file_name, file_path) + os.linesep * 2)
            print('{} [{}]({})'.format('#' * dep, file_name, file_path) + os.linesep * 2, end='')
            walk_dir(file_path, dep + 1)
        elif file_name.endswith('md'):
            OUTPUT_FILE.write('+ [{}]({})'.format(file_name, file_path) + os.linesep)
            print('+ [{}]({})'.format(file_name, file_path) + os.linesep, end='')
    print('')

walk_dir('.', 1)
