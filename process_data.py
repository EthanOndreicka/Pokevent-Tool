import sys
import json
import requests
from bs4 import BeautifulSoup

# Retrieve data from command line arguments
data = sys.argv[1]

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
    start_day = soup.find('span', {'id': 'event-date-start'})
    end_day = soup.find('span', {'id': 'event-date-end'})
    start_time = '10:00am'
    event_image = soup.select('div.image img')


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
    
    print(start_time)

    if event_image:
        for img_tag in event_image:
            event_image_text = "https://leekduck.com" + img_tag['src']
            print("Image URL: ", event_image_text)
    else:
        print('URL Not Found')

    event_details = {"title": event_title.text if event_title else '', "description": [desc.text for desc in description], "starting": start_day_text, "ending": end_day_text, 'startingTime': start_time, 'imageURL': event_image_text}
    
    with open('event_details.json', 'w') as json_file:
        json.dump(event_details, json_file)

# Web scraping spotlight hour page
def spotlightHourParse():
    event_title = soup.find('h1', class_='page-title')
    description = soup.select('div.event-description p')
    start_day = soup.find('span', {'id': 'event-date-start'})
    end_day = soup.find('span', {'id': 'event-date-end'})
    start_time = '6:00pm - 7:00pm'
    event_image = soup.select('div.image img')


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
    
    print(start_time)

    if event_image:
        for img_tag in event_image:
            event_image_text = "https://leekduck.com" + img_tag['src']
            print("Image URL: ", event_image_text)
    else:
        print('URL Not Found')

    event_details = {"title": event_title.text if event_title else '', "description": [desc.text for desc in description], "starting": start_day_text, "ending": end_day_text, 'startingTime': start_time, 'imageURL': event_image_text}
    
    with open('event_details.json', 'w') as json_file:
        json.dump(event_details, json_file)

# Web scraping community day page
def communityDayParse():
    event_title = soup.find('h1', class_='page-title')
    description = soup.select('div.event-description p')
    start_day = soup.find('span', {'id': 'event-date-start'})
    end_day = soup.find('span', {'id': 'event-date-end'})
    start_time = '2:00pm - 5:00pm'
    event_image = soup.select('div.image img')


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
    
    print(start_time)

    if event_image:
        for img_tag in event_image:
            event_image_text = "https://leekduck.com" + img_tag['src']
            print("Image URL: ", event_image_text)
    else:
        print('URL Not Found')

    event_details = {"title": event_title.text if event_title else '', "description": [desc.text for desc in description], "starting": start_day_text, "ending": end_day_text, 'startingTime': start_time, 'imageURL': event_image_text}
    
    with open('event_details.json', 'w') as json_file:
        json.dump(event_details, json_file)

def tierFiveParse():
    event_title = soup.find('h1', class_='page-title')
    description = soup.select('div.event-description p')
    start_day = soup.find('span', {'id': 'event-date-start'})
    end_day = soup.find('span', {'id': 'event-date-end'})
    start_time = '10:00am'
    event_image = soup.select('div.image img')


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
    
    print(start_time)

    if event_image:
        for img_tag in event_image:
            event_image_text = "https://leekduck.com" + img_tag['src']
            print("Image URL: ", event_image_text)
    else:
        print('URL Not Found')

    event_details = {"title": event_title.text if event_title else '', "description": [desc.text for desc in description], "starting": start_day_text, "ending": end_day_text, 'startingTime': start_time, 'imageURL': event_image_text}
    
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
