# Script: Ops 301 Class 01 Ops Challenge Solution
# Author: James Moring
# Date of latest revision: 9/15/2022
# Purpose: Prompt the user to type a string input as the variable for your destination URL.


#Main

#!/usr/bin/env python3

from secrets import choice
import requests

user_URL= input("Type in a URL;")


choice = input("Select a HTTP method")

if choice == 'get':
        method = requests.get
elif choice == 'post':
        method = requests.post
elif choice == 'put':
        method = requests.put
elif choice == 'delete':
        method = requests.delete
elif choice== 'head':
        method = requests.head
elif choice == 'patch':
        method = requests.patch
elif choice == 'options':
        method =requests.options
else:
    print("invalid selection; a get request has been selected")
    method = requests     
