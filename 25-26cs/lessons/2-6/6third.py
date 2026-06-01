#!/usr/bin/python

# 11/02/2026
# Sougato

import os

filename = input("Input filename: ")

ext = os.path.splitext(filename)[-1]

print(f"Extension for {filename} is {ext}.")
