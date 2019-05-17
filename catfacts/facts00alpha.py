#!/usr/bin/env python3

import json
import requests

def main():
    """ Run time code """
    # create r, which is our request object
    r = requets.get("https://cat-facts.herokuapp.com/facts")

    # display the methods available to our new object
    print(dir(r))

main()
