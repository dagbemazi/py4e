#!/usr/bin/python3

"""
Author: Dickson Agbemazi

Description: This program extracts comment counts from 
an XML file given via a URL. The program adds up all the
counts and outputs a total.
"""

import xml.etree.ElementTree as ET
import urllib.request


def count_extractor(url):

    xml_data = urllib.request.urlopen(url)

    my_tree = ET.parse(xml_data)

    total = 0
    for x in my_tree.findall(".//comment"):
        count = x.find("count").text
        total += int(count)

    return total


url_link = input("Enter URL: ")

total_count = count_extractor(url_link)
print(total_count)
