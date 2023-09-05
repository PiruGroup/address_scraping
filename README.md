# Address Scraping from Substandard Home Map

## General Info
Map URL: https://www.arcgis.com/apps/View/index.html?appid=2ba04d4240cb4c8a8affbee5d6541d70

Address JSON URL (this is where the addresses get called to populate the map):
https://www.arcgis.com/sharing/rest/content/items/ebc9cd0f9f1c483c832562e4879e43c3/data?f=json

Python Program which scrapes the map website for addresses: address_parse.py
Current List of Addresses: addresses.csv

## Operation
To run the Python Program on Mac or Linux:

In the command line run

$python3 address_parse.py

A csv file should be created in the working folder
