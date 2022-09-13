# Script: Ops 301 Class 01 Ops Challenge Solution
# Author: James Moring
# Date of latest revision: 9/12/2022
# Purpose: Create an if statement using logical conditionals below
# Code was derived from https://devqa.io/python-conditional-statements-if-else-elif/

#Main

a = 5
b = 5
c = 5

if a != b and b != c and a != c:
    print('This is a scalene triangle')
elif a == b and b == c:
    print('This is an equilateral triangle')
else:
    print('This is an isosceles triangle')

#End