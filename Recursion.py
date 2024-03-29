import requests

from bs4 import BeautifulSoup

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--url", help="Enter the target URL")
'''parser.add_argument("--depth", help="Enter desired depth for web crawler to search")'''
args = parser.parse_args()

urls = []


def crawl(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    all_links = soup.find_all('a')

    for link in all_links:
        link = link.get('href')
        title = soup.find('title')

        if link.startswith("/"):
            url = url + link

        if url not in urls:
            urls.append(url)
            print(title.string)
            print(url)
            crawl(url)



site = args.url


crawl(site)
