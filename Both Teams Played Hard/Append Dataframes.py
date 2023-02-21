#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 23:48:34 2023
Python scripts to scrape data where an NBA team and an NHL team played on the same day over the last ten years and then append all the results into one CSV
@author: brandanclark
"""

import pandas as pd

#Create list of file names
file_names = [
"/Users/brandanclark/Documents/Sports Projects/2023/Both Teams Played Hard/Merged Results/merged_results_ARI.csv",
"/Users/brandanclark/Documents/Sports Projects/2023/Both Teams Played Hard/Merged Results/merged_results_BOS.csv",
"/Users/brandanclark/Documents/Sports Projects/2023/Both Teams Played Hard/Merged Results/merged_results_CHI.csv",
"/Users/brandanclark/Documents/Sports Projects/2023/Both Teams Played Hard/Merged Results/merged_results_DAL.csv",
"/Users/brandanclark/Documents/Sports Projects/2023/Both Teams Played Hard/Merged Results/merged_results_DEN.csv",
"/Users/brandanclark/Documents/Sports Projects/2023/Both Teams Played Hard/Merged Results/merged_results_DET.csv",
"/Users/brandanclark/Documents/Sports Projects/2023/Both Teams Played Hard/Merged Results/merged_results_GSW.csv",
"/Users/brandanclark/Documents/Sports Projects/2023/Both Teams Played Hard/Merged Results/merged_results_LAC.csv",
"/Users/brandanclark/Documents/Sports Projects/2023/Both Teams Played Hard/Merged Results/merged_results_LAL.csv",
"/Users/brandanclark/Documents/Sports Projects/2023/Both Teams Played Hard/Merged Results/merged_results_MIA.csv",
"/Users/brandanclark/Documents/Sports Projects/2023/Both Teams Played Hard/Merged Results/merged_results_MIN.csv",
"/Users/brandanclark/Documents/Sports Projects/2023/Both Teams Played Hard/Merged Results/merged_results_NYI.csv",
"/Users/brandanclark/Documents/Sports Projects/2023/Both Teams Played Hard/Merged Results/merged_results_NYR.csv",
"/Users/brandanclark/Documents/Sports Projects/2023/Both Teams Played Hard/Merged Results/merged_results_PHI.csv",
"/Users/brandanclark/Documents/Sports Projects/2023/Both Teams Played Hard/Merged Results/merged_results_TOR.csv",
"/Users/brandanclark/Documents/Sports Projects/2023/Both Teams Played Hard/Merged Results/merged_results_WAS.csv"
]

#Empty list to store DataFrames
dfs =[]

# Loop through file names, read in each CSV file, and append to the dfs list
for file_name in file_names:
    df = pd.read_csv(file_name)
    dfs.append(df)

# Concatenate all DataFrames into a single DataFrame
merged_df = pd.concat(dfs, ignore_index=True)

# Export the merged DataFrame to a new CSV file
merged_df.to_csv('all_merged_results.csv', index=False)

# Print some information about the merged DataFrame
print(f'Total number of rows: {len(merged_df)}')
print(f'Total number of columns: {len(merged_df.columns)}')
print(f'Column names: {list(merged_df.columns)}')
