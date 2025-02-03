"""
Scrapes legal information from the web.
"""

from bs4 import BeautifulSoup
import requests


def build_headers():
  """
  Builds the headers for the legal information.
  """
  headers = {
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'en-US,en;q=0.9',
    'cache-control':'max-age=0',
    'cookie':'PHPSESSID=9p1e73mm2r7m3f6fad1tln7i5c',
    'dnt':'1',
    'priority':'u=0, i',
    'referer':'https://sldsystem.com/caselawsearch.php?view=citation',
    'sec-ch-ua':'"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"macOS"',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
  }
  return headers

def get_text_from_url(url):
  """
  Given a URL, returns the text of the page.
  """
  response = requests.get(url, timeout=5, headers=build_headers())
  soup = BeautifulSoup(response.text, 'html.parser')
  # get text from the table element
  my_table = soup.find('table')
  return my_table.get_text()

def get_legal_info():
  """
  Scrapes legal information from the web.
  """
  for my_in in range(1, 1000000):
    try:
      url = f'https://sldsystem.com/caseprint.php?id={my_in}'
      my_text = get_text_from_url(url)
      # save the text to a file
      with open(f'legal_info_{my_in}.txt', 'w') as f:
        f.write(my_text)
    except:
      print(f'Failed for {my_in}')
      continue

if __name__ == '__main__':
  get_legal_info()
