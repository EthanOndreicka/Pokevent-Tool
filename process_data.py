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

global url
url = parsed_data['name']
global r
r = requests.get(url)
global soup
soup = BeautifulSoup(r.content, 'html5lib')

def defaultEventParse():
    event_title = soup.find('h1', class_='page-title')
    description = soup.select('div.event-description p')

    if event_title:
        print("Title: " + event_title.text)
    else:
        print('Title not found :(')

    for desc in description:
        print("Description: " + desc.text)

    event_details = {"title": event_title.text if event_title else '', "description": [desc.text for desc in description], "URL": url}
    
    with open('event_details.json', 'w') as json_file:
        json.dump(event_details, json_file)

# Web scraping spotlight hour page
def spotlightHourParse():
    event_title = soup.find('h1', class_='page-title')
    description = soup.select('div.event-description p')

    if event_title:
        print("Title: " + event_title.text)
    else:
        print('Title not found :(')

    for desc in description:
        print("Description: " + desc.text)

    event_details = {"title": event_title.text if event_title else '', "description": [desc.text for desc in description]}
    
    with open('event_details.json', 'w') as json_file:
        json.dump(event_details, json_file)

# Web scraping community day page
def communityDayParse():
    event_title = soup.find('h1', class_='page-title')
    description = soup.select('div.event-description p')
    start_day = soup.find('span', {'id': 'event-date-start'})
    end_day = soup.find('span', {'id': 'event-date-end'})

    if event_title:
        print("Title: " + event_title.text)
    else:
        print('Title not found :(')

    for desc in description:
        print("Description: " + desc.text)

    if start_day:
        start_day_text = start_day.get_text(strip=True)
        start_day_text = start_day_text[:-1]
        print('Start date: ' + str(start_day_text))
    else:
        print('Start date not found')
    
    if end_day:
        end_day_text = end_day.get_text(strip=True)
        end_day_text = end_day_text[:-1]
        print('End date: ' + str(end_day_text))
    else:
        print('End date not found')
        

    event_details = {"title": event_title.text if event_title else '', "description": [desc.text for desc in description], "starting": start_day_text, "ending": end_day_text}
    
    with open('event_details.json', 'w') as json_file:
        json.dump(event_details, json_file)

def tierFiveParse():
    event_title = soup.find('h1', class_='page-title')
    description = soup.select('div.event-description p')

    if event_title:
        print("Title: " + event_title.text)
    else:
        print('Title not found :(')

    for desc in description:
        print("Description: " + desc.text)

    event_details = {"title": event_title.text if event_title else '', "description": [desc.text for desc in description]}
    
    with open('event_details.json', 'w') as json_file:
        json.dump(event_details, json_file)

if (parsed_data['eventType'] == 'SpotlightHour'):
    spotlightHourDetails = spotlightHourParse()
elif (parsed_data['eventType'] == 'CommunityDay'):
    communityDayDetails = communityDayParse()
elif (parsed_data['eventType'] == 'Default'):
    defaultEventDetails = defaultEventParse()
elif (parsed_data['eventType'] == 'Tier5Raid'):
    tierFiveRaidDetails = tierFiveParse()
else:
    print('No choice selected')

#url = 'https://leekduck.com/events/february-communityday2024/'
