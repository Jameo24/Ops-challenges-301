!/bin/bash
# Script: Ops 301 Class 01 Ops Challenge Solution
# Author: James Moring
# Date of latest revision: 9/02/2022
# Purpose: Write a log clearing bash script 

# Main

# How to view a file's contents
cat testfile.txt
# How to clear a file's contents
cat /dev/null > testfile.txt
#Print to screen the before and after of the contents of each file.
echo "print the last 10 lines of the log"
tail /var/log/syslog

echo "delete log"
cat /dev/null > syslog

echo "nothing from log should appear if successful"
tail syslog
#Print User Log in Information
echo "print the last 10 lines of the log in information"
tail /var/log/syslog

echo "delete log in information"
cat /dev/null > syslog

echo "no log in information should appear if successful"
tail syslog

# End