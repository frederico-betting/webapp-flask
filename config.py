"""
SampleNote v1 (https://samplenote.github.io/).

Repository: https://github.com/SampleNote/samplenote-data
Documentation: https://samplenote.github.io/docs/
"""
from os import path

ROOT_DIR = path.dirname(path.abspath(__file__))
VERSION_FILE_PATH = path.join(ROOT_DIR, "version.txt")

with open(file=VERSION_FILE_PATH, mode='r', encoding="utf-8") as version_file:
    VERSION = version_file.read().strip()
