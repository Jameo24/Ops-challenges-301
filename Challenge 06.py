
#Author      James Moring
#Date of last revision  09/12/2022
#Declaration of variables 
#Declaration of functions

# How to use Linux/Bash commands within Python
# First import the os library
import os

# Then use os.system to call any kind of bash command
bashCommand1 = "ls"
bashCommand2 = "whoami"
bashCommand3 = "ip a"
bashCommand4 = "lshw -short"

def systemcall(commandarg):
    print("running system command: " + commandarg)
    os.system(commandarg)



#Main
print("Welcome to Python!")
systemcall(bashCommand1)
systemcall(bashCommand2)
systemcall(bashCommand3)
systemcall(bashCommand4)
#End