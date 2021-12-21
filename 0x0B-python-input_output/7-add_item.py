#!/usr/bin/python3
"""Addng all arguments to a Python list and save them to a file."""
import sys

if __name__ == "__main__":
    """
    import 
       function to load from json file.
       function to save to json file after adding the arguments
    """
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
