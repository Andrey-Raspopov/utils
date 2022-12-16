"""
Remove all duplicate lines in the file
"""
import shutil
import sys

FILENAME = sys.argv[1]
shutil.copyfile(FILENAME, f"{FILENAME}.bak")
with open(f"{FILENAME}.bak", encoding="utf-8") as ifile:
    with open(FILENAME, "w", encoding="utf-8") as ofile:
        data = ifile.read().split("\n")
        data = list(set(data))
        data.sort()
        ofile.write("\n".join(data))
