#!/usr/bin/env python3

def main():
    # Read in out list data
    networklists = []
    with open('driverip.txt', 'r') as driverip:
        for sline in driverip: # single line from our file in sline
            # append adds to the end of our list
            # rstrip remove and special charachers on the right of the str
            # split breaks our string into a list
            # the results is we add a list of driver and ip to networklists
            networklists.append(sline.rstrip("\n").split(' '))

    for driverandip in networklists:
        print('SSH to ' + driverandip[1] +' using driver ' + driverandip[0])

    print("New format type")
    for drndip in networklists:
        print(f"SSH to {drndip[1]} using drvier {drndip[0]}")

    driverip.close()
main()

