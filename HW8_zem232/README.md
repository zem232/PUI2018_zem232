# PUI2018 - HOMEWORK 8 - ZEM232

# Part 1: Urban Data Visualization
Data acquisition, wrangling & visualization is produced in the notebook titled "HW8_zem232_Data_Visualization.ipynb" in this repo.


As a graduate student professional, I want to believe that an egg & cheese sandwich is a perfectly healthy choice for most meals, especially if I politely ask for a healthy slap of iceberg and tomatoe slices in between the melted goo of cheddar and buttery toasted bialy. In reality, the quick deli sandwich represents most meals for many New Yorkers' meals who are eating on-the-go between meetings, work, picking up kids, and a barre class. 

Quite frankly, it's shocking how few of my friends, peers and neighbors cook home cooked meals in this city for 
I speculate this is due to sheer lack of time, cooking space, inspiration, or availability of affordable groceries. In my experience, it may be the former and the latter that are a real driver for most people. Home cooked meals 
I have also realized that as more a neighborhood becomes more affluent, many of the smaller grocers and green-delis drop off the map in place of larger grocery stores like Whole Foods or Harvest Market. 

To investigate this theory, I downloaded the dataset of registered businesses in New York City from the NYC Open Data portal. I isolated my search to Brooklyn since I am personally most familiar with this borough. 
Apparently the registered business "type" (denoted as Industry) in the dataset provides is more granular for certain industries (e.g. Laundries, Home Improvement Contractor), however apparently most grocery stores and delis are registered as Tobacco Retail Dealers. Therefore I isolated the Businesses with the words 'grocer', 'food', or 'produce' in the business name to represent the grocery stores, and isolated the Businesses with the words 'deli' or 'bodega' in the business name to represent delis. 

![Alt text](../HW8_zem232/deliorgrocery.jpeg)
### Delis and Groceries by Zip Code
The figure illustrates the spread of delis and groceries by Zip Code. Upon initial glance, there is no apparent "winner" in terms of which appears more. 


![Alt text](../HW8_zem232/deli&grocery.jpeg)
### Delis, Groceries, and Deli-Groceries by Zip Code
The figure illustrates the spread of delis, groceries and deli-groceries by Zip Code. Deli-groceries occupy a bit of a gray area, since the existence of green delis are very prevelant in certain neighborhoods. However, #upon personal experience#- not all of these so-called grocery-delis sell produce, and are merely a delis with a misleading name (selling a banana and apple DOES NOT give grocery cred!). For the purpose of this analysis, I am interested in the availability of fresh produce to cook a healthy meal. 

![Alt text](../HW8_zem232/ratiodgtopublicassistance.jpeg)
### Scatterplot of Deli/Grocery Ratio vs. the % of Population Receiving Public Assistance in Brooklyn Zip Codes
The plot aims to determine a correlation between the ratio of delis to grocery stores in neighborhoods in Brooklyn, based on the total percentage of people recieving public assistance. The scatterplot looks like a starry sky at best. This data would be more interesting to look at on a more granular basis, which can be achieved by looking at census tract or PUMA regions. 

![Alt text](../HW8_zem232/bk-deli-grocery.jpeg)
### Visualizing Spread of Delis/Groceries and Socioeconomic Factors in Neighborhoods of Brooklyn



# Part 2: Citibike Miniproject

