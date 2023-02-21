#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 23:48:34 2023
Python scripts to scrape data where an NBA team and an NHL team played on the same day over the last ten years
City: Los Angeles [Lakers, Clippers, Kings]
@author: brandanclark
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Create an empty list to store the data for all years
all_data_NBA_LAC = []

# Loop through each year from 2012 to 2023
for year in range(2012, 2024):
    # Set the URL to scrape for the current year
    url = f' https://www.basketball-reference.com/teams/LAC/{year}_games.html'

    # Use requests to download the page HTML
    response = requests.get(url)

    # Use BeautifulSoup to parse the HTML and extract the table of games
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', attrs={'id': 'games'})

    # Find all rows in table
    rows = table.find_all("tr")

    # Create data list for scraped data for current year
    data =[]

    # Loop through each row in the table and append the data to the data list
    for row in rows:
        cells = row.find_all('td')
        if cells:
            NBATeam = 'LAC'
            NBAdate = cells[0].text
            NBAstart = cells[1].text
            NBAopponent = cells[5].text
            NBAresult = cells[6].text
            NBAteamscore = cells[8].text
            NBAopponentscore = cells[9].text
            data.append([NBATeam, NBAdate, NBAstart, NBAopponent, NBAresult, NBAteamscore, NBAopponentscore])

    # Create a DataFrame for the data for the current year
    df = pd.DataFrame(data, columns=["NBA Team", "Date", "Start", "Opponent", "Result", "Team Score", "Opponent Score"])
    
    # Convert the 'Date' Column to datetime data type
    df['Date'] = pd.to_datetime(df['Date'])
    
    #format the 'Date' column as 'yyy-mm-dd'
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

    # Add the DataFrame for the current year to the list of all data
    all_data_NBA_LAC.append(df)

# Combine all DataFrames into a single DataFrame
final_df_NBA_LAC = pd.concat(all_data_NBA_LAC, ignore_index=True)

# Print the first few rows of the final DataFrame
print(final_df_NBA_LAC.head())

#export final_df to csv
final_df_NBA_LAC.to_csv('final_df_NBA_LAC.csv', index=False)



# Run the same code but for the NHL
# Create an empty list to store the data for all years
all_data_NHL_LAK = []

# Loop through each year from 2012 to 2023
for year in range(2012, 2024):
    # Set the URL to scrape for the current year
    url = f' https://www.hockey-reference.com/teams/LAK/{year}_games.html'
   

    # Use requests to download the page HTML
    response = requests.get(url)

    # Use BeautifulSoup to parse the HTML and extract the table of games
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', attrs={'id': 'games'})

    # Find all rows in table
    rows = table.find_all("tr")

    # Create data list for scraped data for current year
    data =[]

    # Loop through each row in the table and append the data to the data list
    for row in rows:
        cells = row.find_all('td')
        if cells:
            #adjustment for change in table structure by Pro Hockey Reference in the 2022-2023 season
            if '2023' in url:
                NHLteam = 'LAK'
                NHLdate = cells[0].text
                NHLopponent = cells[3].text
                NHLresult = cells[6].text
                NHLteamscore = cells[4].text
                NHLopponentscore = cells[5].text
            else:
                NHLTeam = 'LAK'
                NHLdate = cells[0].text
                NHLopponent = cells[2].text
                NHLresult = cells[5].text
                NHLteamscore = cells[3].text
                NHLopponentscore = cells[4].text
            data.append([NHLTeam, NHLdate, NHLopponent, NHLresult, NHLteamscore, NHLopponentscore])

    # Create a DataFrame for the data for the current year
    df = pd.DataFrame(data, columns=["NHL Team", "Date", "Opponent", "Result", "Team Score", "Opponent Score"])

    # Add the DataFrame for the current year to the list of all data
    all_data_NHL_LAK.append(df)

# Combine all DataFrames into a single DataFrame
final_df_NHL_LAK = pd.concat(all_data_NHL_LAK, ignore_index=True)

# Print the first few rows of the final DataFrame
print(final_df_NHL_LAK.head())

#export final_df to csv
final_df_NHL_LAK.to_csv('final_df_NHL_LAK.csv', index=False)

# Create Merged df to show occassions that both teams played
merged_df = pd.merge(final_df_NHL_LAK, final_df_NBA_LAC, on='Date', how='inner')

print(merged_df.head())


# Create a new dataframe with just the LAKumns we care about
result_df = merged_df[['Date', 'NHL Team', 'Opponent_x', 'Result_x', 'Team Score_x', 'Opponent Score_x', 'NBA Team', 'Opponent_y', 'Result_y', 'Team Score_y', 'Opponent Score_y']]

# Rename the columns to make them easier to understand
result_df.columns = ['Date', 'NHL Team', 'NHL Opponent', 'NHL Result', 'NHL Team Score', 'NHL Opponent Score', 'NBA Team', 'NBA Opponent', 'NBA Result', 'NBA Team Score', 'NBA Opponent Score']

# Sort the dataframe by date
result_df = result_df.sort_values(by='Date')

# Print the resulting dataframe
print(result_df)

# Export result_df to CSV
result_df.to_csv('merged_results_LAC.csv', index=False)

# create a copy of the result_df dataframe
result_copy = result_df.copy()

# filter the dataframe to select only rows where both teams won
both_won = result_copy[(result_copy['NHL Result'] == 'W') & (result_copy['NBA Result'] == 'W')]

# filter the dataframe to select only rows where both teams lost
both_lost = result_copy[(result_copy['NHL Result'] == 'L') & (result_copy['NHL Result'] == 'L')]

# print the results
print("Both teams won on these occasions:")
print(both_won)

print("\nBoth teams lost on these occasions:")
print(both_lost)

