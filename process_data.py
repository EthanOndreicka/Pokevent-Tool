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
print('Radio Value: ', parsed_data['eventType'])

url = parsed_data['name']
global r
r = requests.get(url)
global soup
soup = BeautifulSoup(r.content, 'html5lib')

def defaultEventParse():
    event_title = soup.find('h1', class_='page-title')
    description = soup.select('div.event-description p')
    for title in event_title:
        print("Title: " + title.text)
    for desc in description:
        print("Description: " + desc.text) 

# Web scraping spotlight hour page
def spotlightHourParse():
    sub_header = soup.find('h1', class_='page-title')
    description = soup.select('div.event-description p')
    if sub_header:
        print('Title: ' + sub_header.text)
    else:
        print('Sub header not found :(')

    for desc in description:
        print("Description: " + desc.text)

# Web scraping community day page
def communityDayParse():
    sub_header = soup.find('h1', class_='page-title')
    description = soup.select('div.event-description p')
    if sub_header:
        print('Title: ' + sub_header.text)
    else:
        print('Sub header not found :(')

    for desc in description:
        print("Description: " + desc.text)

def tierFiveParse():
    print('t5')

if (parsed_data['eventType'] == 'SpotlightHour'):
    spotlightHourDetails = spotlightHourParse()
elif (parsed_data['eventType'] == 'CommunityDay'):
    communityDayDetails = communityDayParse()
elif (parsed_data['eventType'] == 'Default'):
    communityDayDetails = communityDayParse()
else:
    print('working on it')

#url = 'https://leekduck.com/events/february-communityday2024/'
