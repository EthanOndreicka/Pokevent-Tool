import sys
import json
import requests
from bs4 import BeautifulSoup

# Retrieve data from command line arguments
data = sys.argv[1]

# Process the data (you can replace this with your logic)
print("Received data from Electron app:")
print(data)

parsed_data = json.loads(data)
print('Link: ', parsed_data['name'])

#url = 'https://leekduck.com/events/february-communityday2024/'
url = parsed_data['name']
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')

sub_header = soup.find('h1', class_='page-title')
description = soup.select('div.event-description p')
if sub_header:
    print('Title: ' + sub_header.text)
else:
    print('Sub header not found :(')

for desc in description:
    print("Description: " + desc.text)