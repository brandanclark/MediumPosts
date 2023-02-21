#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 23:48:34 2023

@author: brandanclark
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Create an empty list to store the data for all years
all_data_nuggs = []

# Loop through each year from 2012 to 2023
for year in range(2012, 2024):
    # Set the URL to scrape for the current year
    url = f'https://www.basketball-reference.com/teams/DEN/{year}_games.html'

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
            date = cells[0].text
            start = cells[1].text
            opponent = cells[5].text
            result = cells[6].text
            nuggetsscore = cells[8].text
            opponentscore = cells[9].text
            data.append([date, start, opponent, result, nuggetsscore, opponentscore])

    # Create a DataFrame for the data for the current year
    df = pd.DataFrame(data, columns=["Date", "Start", "Opponent", "Result", "Nuggets Score", "Opponent Score"])
    
    # Convert the 'Date' Column to datetime data type
    df['Date'] = pd.to_datetime(df['Date'])
    
    #format the 'Date' column as 'yyy-mm-dd'
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

    # Add the DataFrame for the current year to the list of all data
    all_data_nuggs.append(df)

# Combine all DataFrames into a single DataFrame
final_df_nuggs = pd.concat(all_data_nuggs, ignore_index=True)

# Print the first few rows of the final DataFrame
print(final_df_nuggs.head())

#export final_df to csv
final_df_nuggs.to_csv('final_df_nuggs.csv', index=False)


# Run the same code but for the Avalanche

# Create an empty list to store the data for all years
all_data_avs = []

# Loop through each year from 2012 to 2023
for year in range(2012, 2024):
    # Set the URL to scrape for the current year
    url = f' https://www.hockey-reference.com/teams/COL/{year}_games.html'
   

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
                date = cells[0].text
                opponent = cells[3].text
                result = cells[6].text
                avsscore = cells[4].text
                opponentscore = cells[5].text
            else:
                date = cells[0].text
                opponent = cells[2].text
                result = cells[5].text
                avsscore = cells[3].text
                opponentscore = cells[4].text
            data.append([date, opponent, result, avsscore, opponentscore])

    # Create a DataFrame for the data for the current year
    df = pd.DataFrame(data, columns=["Date", "Opponent", "Result", "Avs Score", "Opponent Score"])

    # Add the DataFrame for the current year to the list of all data
    all_data_avs.append(df)

# Combine all DataFrames into a single DataFrame
final_df_avs = pd.concat(all_data_avs, ignore_index=True)

# Print the first few rows of the final DataFrame
print(final_df_avs.head())

#export final_df to csv
final_df_avs.to_csv('final_df_avs.csv', index=False)

# Create Merged df to show occassions that both teams played
merged_df = pd.merge(final_df_avs, final_df_nuggs, on='Date', how='inner')

# Create a new dataframe with just the columns we care about
result_df = merged_df[['Date', 'Avs Score', 'Opponent_x', 'Result_x', 'Nuggets Score', 'Opponent_y', 'Result_y']]

# Rename the columns to make them easier to understand
result_df.columns = ['Date', 'Avs Score', 'Avs Opponent', 'Avs Result', 'Nuggets Score', 'Nuggets Opponent', 'Nuggets Result']

# Sort the dataframe by date
result_df = result_df.sort_values(by='Date')

# Print the resulting dataframe
print(result_df)

# Export result_df to CSV
result_df.to_csv('merged_results.csv', index=False)

# create a copy of the result_df dataframe
result_copy = result_df.copy()

# filter the dataframe to select only rows where both teams won
both_won = result_copy[(result_copy['Avs Result'] == 'W') & (result_copy['Nuggets Result'] == 'W')]

# filter the dataframe to select only rows where both teams lost
both_lost = result_copy[(result_copy['Avs Result'] == 'L') & (result_copy['Nuggets Result'] == 'L')]

# print the results
print("Both teams won on these occasions:")
print(both_won)

print("\nBoth teams lost on these occasions:")
print(both_lost)