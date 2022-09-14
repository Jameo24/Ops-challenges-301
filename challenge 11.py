# Script: Ops 301 Class 01 Ops Challenge Solution
# Author: James Moring
# Date of latest revision: 9/13/2022
# Purpose: Using file handling commands, create a Python script that creates a new .txt file, appends three lines, prints to the screen the first line, then deletes the .txt file.


#Main

#!/usr/bin/env python3


import os

# Create a new file if it does not exist
f = open("Fruits.txt", "w")

# How to open a file
f = open("Fruits.txt")

f= open("Fruits.txt", "w")
L = ["Apple\n", "mangos \n", "Banana"]
f.writelines(L)
f.close()

f= open("Fruits.txt", "a")
f.write("\n")
f.write("dragonfruit")

f= open("Fruits.txt", "a")
f.write("\n")
f.write("kiwi")

f= open("Fruits.txt", "a")
f.write("\n")
f.write("peaches")

f = open("Fruits.txt", "r")
print(f.readline())

os.remove("Fruits.txt")



#End