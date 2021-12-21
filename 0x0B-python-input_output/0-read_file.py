#!/usr/bin/python3
"""Defines a text file-reading funtion"""


def read_file(filename=""):
    """Will print the contents of UTF8 text file to stdout"""
    with open(filename, encoding="utf-8") as foo:
        print(foo.read(), end="")
