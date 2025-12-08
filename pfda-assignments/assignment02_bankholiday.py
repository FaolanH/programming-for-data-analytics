#Author: Faolán Hamilton
#Assignment: Write a program called assignment02-bankholdiays.py
# Print out the days bank holidays happen in Northern Ireland, 
#then modify the program to to print the bank holidays that are unique to northern Ireland 
#(i.e. do not happen elsewhere in the UK) you can choose if you want to use the name or 
#the date of the holiday to decide if it is unique.

import requests as rq 
import pandas as pd
import json
from pandas import json_normalize


url = "https://www.gov.uk/bank-holidays.json"
response = rq.get(url)
data =  pd.json_normalize(response.json())


#pretty_data = json.dumps(data, indent=4, sort_keys=True)

#da = json.loads(pretty_data)

#df2 = pd.DataFrame.from_dict(pretty_data, orient ='index')
print(data)

