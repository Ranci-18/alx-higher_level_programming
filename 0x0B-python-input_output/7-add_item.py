#!/usr/bin/python3
"""script adds args to a python list"""
import sys


load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file

try:
    lst = load('add_item.json')
except (FileNotFoundError):
    lst = []

for arg in sys.argv[1:]:
    lst.append(arg)

save(lst, 'add_item.json')
