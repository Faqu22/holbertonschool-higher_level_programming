#!/usr/bin/python3
"""Task 7"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]

try:
    with open('add_item.json') as x:
        data = load_from_json_file('add_item.json')
except FileNotFoundError:
    data = []

data.extend(args)
save_to_json_file(data, 'add_item.json')
