#!/usr/bin/env python3
#Script Name    Directory Creation
#Author         James Moring
#Date of last revision  09/07/2022
#Declaration of variables 
#Declaration of functions

#!/usr/bin/env python3

# Import libraries

import os

# Declaration of variables

dirpath=""


# Declaration of functions

### Declare a function here

def walkfunc(argument):
    for (root, dirs, files) in os.walk(argument):
        print(root)
        print(dirs)
        print(files)

#Main
dirpath = input("Enter directory path") or "/home/jameo24/Ops-challenges-301"
print("The directory path is: " + dirpath)

### Pass the variable into the function here
walkfunc(dirpath)



# End