""" Created by Ashish Shukla on 20 october 2017
This script prints names of all files of type
specified in the given path of
directory and its subdirectories"""

import pathlib
import os
# import sys can use for cmd line arguments


def add_proper(temp_path, nof):
    p = pathlib.Path(temp_path)
    for item in p.iterdir():
        if item.is_file():
            s = str(item)
            l = s.split(".")
            if l[-1] == type_of_file or type_of_file == "":
                print(s)
                nof += 1
        elif item.is_dir():
            nof = add_proper(item, nof)
        else:
            print("alert i don't know about", item)
    return nof


start_path = input("Enter the path: ")  # if nothing given then current working directory
if start_path == "":
    start_path = os.getcwd()
type_of_file = input("Specify type of file: ")
number_of_files = add_proper(start_path, 0)
print(type_of_file, " files in ", start_path, "is", number_of_files)

