#exec_dash.py

import pandas as pd
import os

print("Input file name: ")

input_file = input()

print("/Users/pauldougherty/Desktop/python/p2/" + input_file)

if (os.path.isfile("/Users/pauldougherty/Desktop/python/p2/data/" + input_file)):
    print("file found!")
else:
    print("file not found :(")

