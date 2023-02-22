from __future__ import annotations
import typing as t

import sys
import os
import argparse

def rename_file(file: str) -> None:
    """Rename a file to include its extension

    Args:
        file (str): File to rename
    """

    file = os.path.abspath(file)

    mime = os.popen(f"file --mime-type -b '{file}'").read().strip()
    print(f"{file} -> {mime}")
    ext = mime.split("/")[1]

    if not file.endswith(f".{ext}"):
        os.rename(file, f"{file}.{ext}")

def rename_dir(dir: str) -> None:
    """Rename all files in a directory to include their extension

    Args:
        dir (str): Directory to rename files in
    """
    for file in os.listdir(dir):
        rename_file(os.path.join(dir, file))

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="extensionator", description="Add extensions to files that don't have an extension based on their mime type.")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    sub = subparsers.add_parser("file", help="Add extensions to a single file")
    sub.add_argument("file", help="File to add extension to")

    sub = subparsers.add_parser("dir", help="Add extensions to all files in a directory")
    sub.add_argument("dir", help="Directory to add extensions to")
    sub.

    args = parser.parse_args()

    if args.command == "file":
        rename_file(args.file)

    elif args.command == "dir":
        rename_dir(args.dir)

    else:
        parser.print_help()