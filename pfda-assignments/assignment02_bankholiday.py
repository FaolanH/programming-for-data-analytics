#Author: Faolán Hamilton
#Assignment: Write a program called assignment02-bankholdiays.py
# Print out the days bank holidays happen in Northern Ireland, 
#then modify the program to print the bank holidays that are unique to northern Ireland 
#(i.e. do not happen elsewhere in the UK) you can choose if you want to use the name or 
#the date of the holiday to decide if it is unique.

# I tried a couple different ways including for loops to go about this but unfortunately I had to turn to CoPilot for help! 
# Here is the conversation: https://copilot.microsoft.com/shares/zMsHYuWqBQnBrWtC46fBV
# I asked it to reference it's sources, which interesting I had used a few

import requests as rq 

url = "https://www.gov.uk/bank-holidays.json"
response = rq.get(url)
data = response.json()

# Get the holidays from England & Wales and Scotland
uk_holidays = set()
for event in data["england-and-wales"]["events"]:
    uk_holidays.add((event["title"], event["date"]))

for event in data["scotland"]["events"]:
    uk_holidays.add((event["title"], event["date"]))

# Get the holidays for Northern Ireland
ni_unique_holidays = []
for event in data["northern-ireland"]["events"]:
    if (event["title"], event["date"]) not in uk_holidays:
        # I had also used this method from this source: https://www.geeksforgeeks.org/python/python-get-unique-values-list/
        ni_unique_holidays.append(event)

# Print results
for event in ni_unique_holidays:
    print(f"Unique Northern Ireland Holidays - {event['title']} on {event['date']}")
