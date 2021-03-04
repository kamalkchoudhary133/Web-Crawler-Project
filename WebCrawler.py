# We will first import web libraries/modules that we will require for our web crawler.

# We will use 'Requests' module to send HTTP requests and get required information in response.
import requests

# We will use 'Beautiful Soup' library to get links, headers, titles and other information from a web page.
from bs4 import BeautifulSoup

# We will use 'Argparse' module to make a CLI tool for your web crawler.
import argparse

# Now lets write code for making CLI tool using argparse module.
parser = argparse.ArgumentParser()
parser.add_argument("--url", help="Enter the target URL")
args = parser.parse_args()
# I will try to add more arguments into my CLI tool.

# The following code will help us to get all the links from a given webpage.

# We will first make a HTTP request to the given url.
source_code = requests.get(args.url)
plain_text = source_code.text
# Now we will load it into a Beautiful Soup object.
soup = BeautifulSoup(plain_text, 'html.parser')
urls = []
# Now we will get all links using .findAll() and use "a" tag which the indicator for links in html.
for link in soup.find_all('a'):
    title = link.string
# Now we will create a file which will have all the links and their corresponding titles in it.
    file = open("results.txt", 'a')
    file.write(str(title) + "\n")
    file.write(link.get('href') + "\n")
    file.close()










