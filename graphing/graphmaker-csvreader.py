#!/usr/bin/env python3
#from python std library

import csv
import numpy as np
import matplotlib.pyplot as plt

def parsecsvdata():
    """ returns a list [0] is LAN and [1] Wan data """
    summary =[]

    with open("/home/student/VLab1/myCode/graphing/2018summary.csv", "r") as downtime:
        # parse csv data with csv.reader
        downdata = csv.reader(downtime, delimiter=",")
        for row in downdata:
            rowdata = (row[0], row[1], row[2], row[3])
            summary.append(rowdata)  #add dict to list

    return summary

def main():
    N = 4

    ## grab our data
    summary = parsecsvdata()
    localnetMeans = summary[0]    #LAN data
    wanMeans = summary[1]     # WAN data

    ind = np.arange(N)        # the x locations for the groups
    # the width of the bars: can also be len(x) sequence
    width = 0.5

    # describe where to dispaly pl
    p1 = plt.bar(ind, localnetMeans, width)
    # stack p2 on top of p1
    p2 = plt.bar(ind, wanMeans, width, bottom=localnetMeans)

    # describe the table metadata
    plt.ylabel("Length of Outage (mins)")
    plt.title("2018 Network Summery")
    plt.xticks(ind, ("Q1", "Q2", "Q3", "Q4"))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ("LAN", "WAN"))

    #SAVE the graph
    plt.savefig\
        ("/home/student/VLab1/myCode/graphing/2018summary-csv.png")

main()

