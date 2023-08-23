# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 18:11:02 2023

@author: sambh
"""

import os
import shutil

def copy_files_from_subfolders(src_directory, dest_directory):
    # Ensure the destination directory exists; if not, create it
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    # Walk through src_directory
    for dirpath, dirnames, filenames in os.walk(src_directory):
        for file in filenames:
            # Construct the full file path
            file_path = os.path.join(dirpath, file)
            # Copy each file to the dest_directory
            shutil.copy2(file_path, dest_directory)
            print(f"Copied {file_path} to {dest_directory}")

src_directory = "C:\\Users\\sambh\\Desktop\\count"
dest_directory = "C:\\Users\\sambh\\Desktop\\upload"

copy_files_from_subfolders(src_directory, dest_directory)
