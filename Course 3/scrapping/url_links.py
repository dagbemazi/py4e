#!/usr/bin/python3

"""
Author: Dickson Agbemazi
Course: Py4E, Week 4 Assignment 2
"""

import re
import urllib.request
from bs4 import BeautifulSoup


def scrap_last_link(url, count, index):

    url = url
    counter = 0
    while counter <= (count - 1):
        print(f"Retrieving: {url}")
        # Read webpage as file
        document = urllib.request.urlopen(url)
        # Parse document and find all anchor tags
        soup = BeautifulSoup(document, "html.parser")
        anchors = soup("a")
        # Loop through spans and search for numbers & add to list
       # for pos_link in anchors:
        positional_link = str(anchors[index - 1])
        link = re.search("href=\"(.*)\"", positional_link).group(1)
        counter += 1
        url = link
    return link


def retrieve_last_name():

    linky = input("Enter URL: ")
    count = int(input("Enter count: ")) - 1
    position = int(input("Enter position: "))

    last_link = scrap_last_link(linky, count, position)

    print(f"Retrieving: {last_link}")

    document = urllib.request.urlopen(last_link)
    # Parse document and find all anchor tags
    soup = BeautifulSoup(document, "html.parser")
    anchors = soup("a")
    # Loop through spans and search for numbers & add to list
    # for pos_link in anchors:
    positional_link = str(anchors[position - 1])
    name = re.search(">(.+)<", positional_link).group(1)
    return name


last_name = retrieve_last_name()
print(last_name)
