#!/usr/bin/python3
"""
Author: Dickson Agbemazi

Description: This script extracts INT values from a JSON file,
adds up all the numbers and prints it.
"""
import json
import urllib.request


def count_extractor_json(url):
    json_data = urllib.request.urlopen(url)  # Open URL as file

    load_data = json.load(json_data)  # Load the json data

    total = 0
    for comment in load_data["comments"]:  # Loop through comments
        # Read count key from each dict; convert to int
        total += int(comment["count"])
    return total


url_link = input("Enter URL: ")
total_count = count_extractor_json(url_link)
print(total_count)
