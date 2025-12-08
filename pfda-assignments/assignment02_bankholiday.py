#Author: Faolán Hamilton
#Assignment: Write a program called assignment02-bankholdiays.py
# Print out the days bank holidays happen in Northern Ireland, 
#then modify the program to to print the bank holidays that are unique to northern Ireland 
#(i.e. do not happen elsewhere in the UK) you can choose if you want to use the name or 
#the date of the holiday to decide if it is unique.

import requests as rq 
import pandas as pd
import json
from collections import Counter

url = "https://www.gov.uk/bank-holidays.json"
response = rq.get(url)
data = response.json()

# Source: https://www.geeksforgeeks.org/python/response-json-python-requests/
# https://www.geeksforgeeks.org/python/json-dumps-in-python/
pretty_data = json.dumps(data, indent=4, sort_keys=True)

event_count = sum(len(event["events"]) for event in data["northern-ireland"])
print("Number of chapters:", chapter_count)
# Printing Northern Ireland events
#for event in data ["northern-ireland"]["events"]:
#    print (f"{event['title']} on {event['date']}")

#res = list(dict.fromkeys(data))
#print(res)


'''
    # Printing Northern Ireland events
for event in data ["northern-ireland"]["events"]:
    if event in ["northern-ireland"]:
        unique = False
        break
    ["northern-ireland"].add(event)

print (unique)

        # Check for duplicates
unique = True
for x in a:
    if x in seen:
        unique = False
        break
    seen.add(x)

print(unique)

for event in data["events"]:
    print(f"Event {event['title']} is {'NI' if division['northern-ireland'] else 'N/A'}")

ni = data["northern-ireland"]

for event in data ["northern-ireland"]:
    available_products = [e for e in event if e["northern-ireland"]]
    print(f"Available: {len(available_products)} products")
# I found a StackOverflow page to help me convert this to a dataframe (https://stackoverflow.com/questions/59306252/importing-json-file-url-to-pandas-data-frame)
#df_data = pd.DataFrame.from_dict(data['northern-ireland'])

for event in data ["northern-ireland"]["events"]:
    print (f"{event['title']} on {event['date']}")


print(f"Total products: {len(products)}")

# Source: https://www.freecodecamp.org/news/how-to-parse-json-in-python-with-examples/#heading-how-to-parse-json-arrays

for event in data ["northern-ireland"]:
    status = "Northern Ireland event" if event["northern-ireland"] else "N/A"
    print (f"{event['title']} on {event['date']}")

#print (list(data.scotland))
#data = pd.read_json ("https://www.gov.uk/bank-holidays.json")

#pretty_data = data, indent = 4
#print (pretty_data['northern-ireland']['events'])
'''