#!/usr/bin/env python3

## python3 -m pip install pyexcel
## python3 -m pip install pyexcel-xls
import pyexcel
import datetime as dt

# Request data from user

def get_ip_data():
    input_ip = input("\nWhat is the IP address? ")
    input_driver = input("What is the driver associated with this devices? ")
    d = {"IP": input_ip, "driver": input_driver}
    return d

# Runtime
mylistdict = []   # this will be our list we turn into a *.xls file

print("Hello! This program will make you a *.xls file")

while(True):
    mylistdict.append(get_ip_data())
    keep_going = input("\nWould you like to add another value? Enter to continue, or enter 'q' to quit.")
    if (keep_going.lower() == 'q'):
        break;

today = dt.datetime.now().strftime("%Y-%m-%d")
filename = input("\nWhat is the name of the *.xls file? ")
filename  = today + "." + filename + ".xls"
pyexcel.save_as(records=mylistdict, dest_file_name=filename)
print("The file " + filename + " should be in you local directory")
print(mylistdict)
