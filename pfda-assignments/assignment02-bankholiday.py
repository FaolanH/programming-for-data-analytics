#Author: Faolán Hamilton
#Assignment: Print out the days bank holidays happen in Northern Ireland, 
#then modify the program to to print the bank holidays that are unique to northern Ireland 
#(i.e. do not happen elsewhere in the UK) you can choose if you want to use the name or 
#the date of the holiday to decide if it is unique.

import requests as rq 
import pandas as pd

url = "https://www.gov.uk/bank-holidays.json"
response = rq.get(url)
data = response.json()
# I found a StackOverflow page to help me convert this to a dataframe (https://stackoverflow.com/questions/59306252/importing-json-file-url-to-pandas-data-frame)
df_data = pd.DataFrame.from_dict(data['northern-ireland'])

print (df_data)
#print (list(data.scotland))
#data = pd.read_json ("https://www.gov.uk/bank-holidays.json")

#pretty_data = data, indent = 4
#print (pretty_data['northern-ireland']['events'])
