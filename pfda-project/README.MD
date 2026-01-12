# Author: Faolán Hamilton
# Project for the Programming for Data Analytics module Winter 2025

## Project: Analyse the planning applications submitted to Clare County Council over 2025

#### Project Description - Related to my current work, my undergrad degree and my home county, this is a topic I am very interested in. The development cycle can take upward of 2.5 years from planning application submission to dwelling completion - given the current housing crisis knowing how many applications are currently in the system is very important. All local authorities in the country have also increased their housing targets with new government policy in place. For Clare this has increased from 550 units annually to 985 an increase of 79%.

###### Source: https://assets.gov.ie/static/documents/S.28_Guidelines_-_NPF_Implementation_-_Housing_Growth_Requirements.pdf

#### The dataset I used has planning application data for all 31 local authorities in Ireland going back several decades. This is a very powerful database and a useful tool to understand the recent history of specific sites or areas ([Planning Application Mapping Tool](https://planning.geohive.ie/datasets/housinggovie::irishplanningapplications/explore?filters=eyJQbGFubmluZ0F1dGhvcml0eSI6WyJDbGFyZSBDb3VudHkgQ291bmNpbCJdLCJSZWNlaXZlZERhdGUiOlsxNzM1Njg5NjAwMDAwLDI3MDQyMzM2MDAwMDBdfQ%3D%3D&layer=0)). I downloaded a filtered .csv and .shp (shapefile) of this dataset focusing on applications made in Clare County Council in 2025. 

As this is such a large dataset (nearly half a million records) there is a lot of missing data, inconsistencies across local authorities, duplicates etc. There are elements I would like to have looked at but found the data structure a barrier such as:
- A further analysis on the application type (null residential units) - change of use, ancillary works etc.
- An analysis on the settlements within Clare, possible through the x,y and mapping but not reliable using the address points on Python
- The area of site to determine how many units per hectare is in each site and how it complies with best practise, much of this column was N/A and would have been a limited picture.

#### In this project I have analysed several aspects of Planning Application data in Clare in 2025:
- Planning Application Types (Permission, Permission Consequent, Extension of Duration, Outline Permission and Retention) 
- Decision Status (Granted without conditions (Unconditional), Granted with conditions (Conditional), Refused, Not yet decided)
- Appeals (Conditional, Modified and Refused) 
- Residential Units (number of units applied for, number of units granted)
- Decision Due dates discrepancy between the actual decision date and the deadline expressed


#### All imports for this repository have been included within the notebook:
- datetime
- timedelta
- pandas
- matplotlib
- matplotlib.dates
- matplotlib.lines
- re (regular expressions)

#### For both the maps and graphs, I matched the colours throughout using palettes found on [ColorBrewer](https://colorbrewer2.org/#type=diverging&scheme=RdYlGn&n=5). This ensures a consistent scheme throughout the project