#!/usr/bin/python3
"""
A script that adds all arguments to a Python list
"""

import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    jn_list = load_from_json_file("add_item.json")
except Exception:
    jn_list = []


for i in sys.argv[1:]:
    jn_list.append(i)
save_to_json_file(jn_list, "add_item.json")
