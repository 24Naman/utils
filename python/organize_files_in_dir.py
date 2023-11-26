#!/usr/bin/python3

"""
Python script which uses tkinter and os functions to organise files 
in seperate dir by their creation date
"""

import os
import os.path
from datetime import datetime
import shutil
from tkinter import filedialog


def get_files_src_dir() -> str:
    """Select and return selected direction"""
    return filedialog.askdirectory(title="Select a directory")


def get_creation_date(file_path: str) -> datetime:
    """
    Get creation for the file
    """
    creation_time = os.path.getmtime(file_path)
    return datetime.fromtimestamp(creation_time)


def main():
    """
    Main Function
    """
    src_dir = get_files_src_dir()

    dir_file_list = os.listdir(src_dir)

    print(f"Source Directory -> {src_dir}")
    print(f"File Count -> {len(dir_file_list)}")

    for i, file in enumerate(dir_file_list):
        src_file_path = os.path.join(src_dir, file)
        print(f"Processing {i} / {len(dir_file_list)} -> {src_file_path}")

        if not os.path.isfile(src_file_path):
            continue

        creation_date = get_creation_date(src_file_path)

        destination_directory = os.path.join(src_dir, creation_date.strftime("%Y%m"))
        os.makedirs(destination_directory, exist_ok=True)

        dest_file_path = os.path.join(destination_directory, file)
        shutil.move(src_file_path, dest_file_path)
        print(f"Processed to {i} / {len(dir_file_list)} -> {dest_file_path}")


if __name__ == "__main__":
    main()
