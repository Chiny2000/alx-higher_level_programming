#!/usr/bin/python3
import sys
import json
from os.path import exists
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_item():
    # Check if the file exists, if not, create an empty list
    if exists("add_item.json"):
        my_list = load_from_json_file("add_item.json")
    else:
        my_list = []

    # Add command line arguments to the list
    my_list.extend(sys.argv[1:])

    # Save the updated list to the JSON file
    save_to_json_file(my_list, "add_item.json")

if __name__ == "__main__":
    add_item()
