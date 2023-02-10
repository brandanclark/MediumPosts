#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:21:48 2023
Script to get total data for last 5 full seasons of Premier League fixtures
@author: brandanclark
"""

#import relevant packages
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


#17-18 season
url = "https://fbref.com/en/comps/9/2017-2018/schedule/2017-2018-Premier-League-Scores-and-Fixtures"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the table with the fixtures
table = soup.find("table", {"class": "stats_table"})

# Find all the rows in the table
rows = table.find_all("tr")

# Create data list for scraped data
data = []

# Loop through each row and find the relevant data
for row in rows:
    cells = row.find_all("td")
    if cells:
        day = cells[0].text
        date = cells[1].text
        time = cells[2].text
        home = cells[3].text
        homexG = cells[4].text
        score = cells[5].text
        if "–" in score:
            home_score, away_score = score.split("–")
            total_score = int(home_score)+int(away_score)
        else:
            home_score = None
            away_score = None
            total_score = None
        awayxG = cells[6].text
        away = cells[7].text
        data.append([day, date, time, home, homexG, score, home_score, away_score, awayxG, away, total_score])

# Create a DataFrame from the list of data
df_17_18 = pd.DataFrame(data, columns=["Day", "Date", "Time", "Home Team", "Home xG", "Score", "Home Score", "Away Score", "Away xG", "Away Team", "Total Score"])
     
 
#18-19 season
url = "https://fbref.com/en/comps/9/2018-2019/schedule/2018-2019-Premier-League-Scores-and-Fixtures"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the table with the fixtures
table = soup.find("table", {"class": "stats_table"})

# Find all the rows in the table
rows = table.find_all("tr")

# Create data list for scraped data
data = []

# Loop through each row and find the relevant data
for row in rows:
    cells = row.find_all("td")
    if cells:
        day = cells[0].text
        date = cells[1].text
        time = cells[2].text
        home = cells[3].text
        homexG = cells[4].text
        score = cells[5].text
        if "–" in score:
            home_score, away_score = score.split("–")
            total_score = int(home_score)+int(away_score)
        else:
            home_score = None
            away_score = None
            total_score = None
        awayxG = cells[6].text
        away = cells[7].text
        data.append([day, date, time, home, homexG, score, home_score, away_score, awayxG, away, total_score])

# Create a DataFrame from the list of data
df_18_19 = pd.DataFrame(data, columns=["Day", "Date", "Time", "Home Team", "Home xG", "Score", "Home Score", "Away Score", "Away xG", "Away Team", "Total Score"])


#19-20 season
url = "https://fbref.com/en/comps/9/2019-2020/schedule/2019-2020-Premier-League-Scores-and-Fixtures"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the table with the fixtures
table = soup.find("table", {"class": "stats_table"})

# Find all the rows in the table
rows = table.find_all("tr")

# Create data list for scraped data
data = []

# Loop through each row and find the relevant data
for row in rows:
    cells = row.find_all("td")
    if cells:
        day = cells[0].text
        date = cells[1].text
        time = cells[2].text
        home = cells[3].text
        homexG = cells[4].text
        score = cells[5].text
        if "–" in score:
            home_score, away_score = score.split("–")
            total_score = int(home_score)+int(away_score)
        else:
            home_score = None
            away_score = None
            total_score = None
        awayxG = cells[6].text
        away = cells[7].text
        data.append([day, date, time, home, homexG, score, home_score, away_score, awayxG, away, total_score])

# Create a DataFrame from the list of data
df_19_20 = pd.DataFrame(data, columns=["Day", "Date", "Time", "Home Team", "Home xG", "Score", "Home Score", "Away Score", "Away xG", "Away Team", "Total Score"])
   

#20-21 season
url = "https://fbref.com/en/comps/9/2020-2021/schedule/2020-2021-Premier-League-Scores-and-Fixtures"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the table with the fixtures
table = soup.find("table", {"class": "stats_table"})

# Find all the rows in the table
rows = table.find_all("tr")

# Create data list for scraped data
data = []

# Loop through each row and find the relevant data
for row in rows:
    cells = row.find_all("td")
    if cells:
        day = cells[0].text
        date = cells[1].text
        time = cells[2].text
        home = cells[3].text
        homexG = cells[4].text
        score = cells[5].text
        if "–" in score:
            home_score, away_score = score.split("–")
            total_score = int(home_score)+int(away_score)
        else:
            home_score = None
            away_score = None
            total_score = None
        awayxG = cells[6].text
        away = cells[7].text
        data.append([day, date, time, home, homexG, score, home_score, away_score, awayxG, away, total_score])

# Create a DataFrame from the list of data
df_20_21 = pd.DataFrame(data, columns=["Day", "Date", "Time", "Home Team", "Home xG", "Score", "Home Score", "Away Score", "Away xG", "Away Team", "Total Score"])
  

#21-22 season
url = "https://fbref.com/en/comps/9/2021-2022/schedule/2021-2022-Premier-League-Scores-and-Fixtures"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the table with the fixtures
table = soup.find("table", {"class": "stats_table"})

# Find all the rows in the table
rows = table.find_all("tr")

# Create data list for scraped data
data = []

# Loop through each row and find the relevant data
for row in rows:
    cells = row.find_all("td")
    if cells:
        day = cells[0].text
        date = cells[1].text
        time = cells[2].text
        home = cells[3].text
        homexG = cells[4].text
        score = cells[5].text
        if "–" in score:
            home_score, away_score = score.split("–")
            total_score = int(home_score)+int(away_score)
        else:
            home_score = None
            away_score = None
            total_score = None
        awayxG = cells[6].text
        away = cells[7].text
        data.append([day, date, time, home, homexG, score, home_score, away_score, awayxG, away, total_score])

# Create a DataFrame from the list of data
df_21_22 = pd.DataFrame(data, columns=["Day", "Date", "Time", "Home Team", "Home xG", "Score", "Home Score", "Away Score", "Away xG", "Away Team", "Total Score"])
 

#22-23 season
url = "https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the table with the fixtures
table = soup.find("table", {"class": "stats_table"})

# Find all the rows in the table
rows = table.find_all("tr")

# Create data list for scraped data
data = []

# Loop through each row and find the relevant data
for row in rows:
    cells = row.find_all("td")
    if cells:
        day = cells[0].text
        date = cells[1].text
        time = cells[2].text
        home = cells[3].text
        homexG = cells[4].text
        score = cells[5].text
        if "–" in score:
            home_score, away_score = score.split("–")
            total_score = int(home_score)+int(away_score)
        else:
            home_score = None
            away_score = None
            total_score = None
        awayxG = cells[6].text
        away = cells[7].text
        data.append([day, date, time, home, homexG, score, home_score, away_score, awayxG, away, total_score])

# Create a DataFrame from the list of data
df_22_23 = pd.DataFrame(data, columns=["Day", "Date", "Time", "Home Team", "Home xG", "Score", "Home Score", "Away Score", "Away xG", "Away Team", "Total Score"])
 
 
# Create a list of all the dataframes
df_list = [df_17_18, df_18_19, df_19_20, df_20_21, df_21_22, df_22_23]

# Use pd.concat to combine dataframes into one
final_df = pd.concat(df_list)

#drop blank rows
#final_df['Total Score'].replace('', np.nan, inplace=True)
final_df.dropna(subset=['Total Score'], inplace = True)

#check types of data
final_df.dtypes


#convert date and time columns to datetime
final_df['Date'] = pd.to_datetime(final_df['Date'], format='%Y-%m-%d').dt.date
final_df['Time']=pd.to_datetime(final_df['Time'], format='%H:%M', exact=False).dt.time

#create new column called Hour to group kickoff times by hour
final_df['Hour'] = final_df['Time'].dt.hour

#export final_df to csv
final_df.to_csv('final_df.csv', index=False)

#begin plotting work
import matplotlib.pyplot as plt

# Create a pivot table to aggregate the total score by time
pivot = final_df.pivot_table(index='Hour', values='Total Score', aggfunc='mean')

# Plot the pivot table as a bar chart
pivot.plot(kind='bar', figsize=(10, 5))

# Add a title to the chart
plt.title("Average Total Score by Game Hour - Premier League Last 5 Complete Seasons")

# Show the chart
plt.show()

