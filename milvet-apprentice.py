#!/usr/bin/env python3
import os
import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime

import smtp
import pages_dict

# HTTP GET function
def http_get(url=''):
  count = 0
  while (count < 3):
    try:
      res = requests.get(url)
      if res.status_code == 200:
        return res
      else:
        count += 1
        time.sleep(60)
    except requests.exceptions.ConnectionError:
      print('Connection Error: {}').format(res.status_code)
    except requests.exceptions.HTTPError:
      print('HTTP Error: {}').format(res.status_code)

# uses pages_dict.py to crawl target pages
def task():
  companies = []
  message = ''

  # iterate through multidimentional pages dictionary
  for key, data in pages_dict.items():
    url = data['url']
    page = http_get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    availability = eval(data['availability'])
    condition = data['condition']
    
    # appends job/apprenticeship info to email message string if availability is detected
    if condition not in availability:
      companies.append('\n' + key + '\n')
      companies.append("Link: " + url + '\n')
      message = ''.join(companies)
          
  if companies:
    smtp.message += message
    smtp.send()

if __name__ == '__main__':
  smtp.login()
  task()
  with open ('/tmp/cron.log', 'a+') as f:
    f.write('milvet-apprentice.py: Last ran at {}\n'.format(datetime.now()))
