# We will first import web libraries/modules that we will require for our web crawler.

# We will use 'Requests' module to send HTTP requests and get required information in response.
import requests

# We will use 'Beautiful Soup' library to get links, headers, titles and other information from a web page.
from bs4 import BeautifulSoup

# We will use 'Argparse' module to make a CLI tool for your web crawler.
import argparse

# Now lets write code for making CLI tool using argparse module.

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help="Enter the target URL")
args = parser.parse_args()

# I will try to add more arguments into my CLI tool.









