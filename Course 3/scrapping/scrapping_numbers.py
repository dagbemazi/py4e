#!/usr/bin/python3
"""
Author: Dickson Agbemazi

This program scraps numbers from HTML table only and adds them up.
It makes use of urllib and beautifulsoup to achieve this.
"""
import urllib.request
from bs4 import BeautifulSoup
import re


def scrap_numbers(url):
    # Read webpage as file
    document = urllib.request.urlopen(url)
    # Parse document and find all spans
    soup = BeautifulSoup(document, "html.parser")
    spans = soup("span")

    numbers = []  # Initialized to store numbers
    # Loop through spans and search for numbers & add to list
    for comment in spans:
        number = re.search("([0-9])+", str(comment)).group()
        numbers.append(int(number))

    total = sum(numbers) # Sum of numbers in list
    return total


response = scrap_numbers(input("Enter - "))
print(response)
