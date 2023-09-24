# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 13:08:54 2023

@author: piotr
"""

# importing necessary modules
import pandas as pd 
import zipfile
import os

# setting working directory 
path = r'D:\PythonVS\FIFA2021'
os.chdir(path)
os.getcwd()

# IMPORT AND CLEAN DATASET

# extracting the file from the downloaded zip file
zipfile_name = 'archive.zip'
with zipfile.ZipFile(zipfile_name, 'r') as file:
    file.extractall()

# checking the content of the zipfile
lst = os.listdir(path)

# reading in the csv file as a pandas dataframe
FIFA = pd.read_csv(lst[1])

# exploring the data
FIFA.head() # checking first 5 rows
FIFA.tail() # checking last 5 rows
FIFA.info() # printing information about data 
FIFA.shape # printing data shape
FIFA # printing FIFA
statistics = FIFA.describe()

# deleting duplicates if exist 
FIFA.drop_duplicates

# Columns to clean: Club, Hits, Joined, Height, Weight, Values, Wage, W/F, SM and IR
# Some of the 77 columns aren't needed so they will be dropped
columns_to_drop = ['photoUrl', 'playerUrl', 'Loan Date End', 'Release Clause']
FIFA = FIFA.drop(columns = columns_to_drop)

# changing the column LongName to FullName
FIFA.rename(columns={'LongName':'FullName'},inplace=True)

# changing the column LongName to FullName
FIFA.rename(columns ={'↓OVA':'OVA'}, inplace = True)

# filling null values with zeros to enable further analysis without deleting the column
FIFA.Hits = FIFA.Hits.fillna('0')
FIFA.info()

# cleaning Club column from \n\n\n\n
FIFA.Club.unique()

# function to delete '\n\n\n\n' values from Club column
def delete_n(delete_str):
    if isinstance(delete_str, str) and '\n\n\n\n' in delete_str:
        return delete_str.replace('\n\n\n\n','')
    else:
        return None  # Handle unexpected formats or None values

# Apply the delete_n function to the 'Club' column
FIFA['Club'] = FIFA['Club'].apply(delete_n)

# Filter out None values
filtered_club = FIFA['Club'].dropna()

# Sort the unique values
unique_club = sorted(filtered_club.unique())

print(unique_club)

# converting Joined column to proper date-time format
FIFA['Joined']
FIFA.Joined.unique()
FIFA['Joined'] = pd.to_datetime(FIFA['Joined'],format = '%b %d, %Y').dt.date
FIFA.rename(columns ={'Joined':'Date'}, inplace = True)

# converting Height column to cm
FIFA.Height.unique()

# function to convert Height values to cm
def convert_to_cm(height_str):
    if 'cm' in height_str:
        # extract the numeric part (height in centimeteres)
        return int(height_str.split('cm')[0])
    elif '\'' in height_str:
        # extract feet and inches and convert to centimeters
        parts = height_str.split('\'')
        feet = int(parts[0])
        inches = int(parts[1].replace('"',''))
        # convert feet and inches to centimeters (1 foot = 30.48cm, 1 inch = 2.54cm)        
        return round(feet * 30.48 + inches * 2.54)
    else:
        return None # Handle unexpected formats
# apply the conversion function to the 'Height' column
FIFA['Height'] = FIFA['Height'].apply(convert_to_cm)
FIFA.rename(columns ={'Height':'Height(cm)'}, inplace = True)
unique_heights = sorted(FIFA['Height(cm)'].unique())
print(unique_heights)

# converting Weight to kg
FIFA.Weight.unique()

# function to convert Weight values to kg

def convert_to_kg(weight_str):
    if 'kg' in weight_str:
        # extract the numeric part (weight in kilograms)
        return int(weight_str.split('kg')[0])
    elif 'lbs' in weight_str:
        # extract lbs and convert to kilograms
        parts = weight_str.split('lbs')
        weight = int(parts[0])
        # convert lbs to kilograms
        return round(weight * 0.45359237)
    else:
        return None # Handle unexpected formats 

# apply the conversion function to the 'Height' column
FIFA['Weight'] = FIFA['Weight'].apply(convert_to_kg)
FIFA.rename(columns ={'Weight':'Weight(kg)'}, inplace = True)
unique_weights = sorted(FIFA['Weight(kg)'].unique())
print(unique_weights)

# Preferred Foot column check
unique_foot = sorted(FIFA['Preferred Foot'].unique())
print(unique_foot)

# converting Value to millions 
unique_value = sorted(FIFA['Value'].unique())
print(unique_value)

# function to convert Value to values in millions

def convert_to_million(value_str):
    try:
        # Check if the input is a string (for values like "0.15M" or "1.2K")
        if isinstance(value_str, str):
            if 'M' in value_str:
                # Extract the numeric part and currency (value in millions)
                return float(value_str.replace('€', '').replace('M', ''))
            elif 'K' in value_str:
                # Remove '€' and 'K', convert to float, and divide by 1000 (values in millions)
                value = float(value_str.replace('€', '').replace('K', ''))
                return round(value / 1000, 2)  # Convert thousands to millions (2 decimal places)
            else:
                value = float(value_str.replace('€', ''))
                return value  # Handle unexpected formats
        else:
            # Input is already a float, return it as is
            return value_str
    except Exception as e:
        print(f"Error processing value: {value_str}")
        print(e)
        return None

# apply the conversion function to the 'Value' column
FIFA['Value'] = FIFA['Value'].apply(convert_to_million)
FIFA.rename(columns = {'Value':'Value(€M)'}, inplace = True)
FIFA['Value(€M)'] = FIFA['Value(€M)'].astype(float)  
unique_values = sorted(FIFA['Value(€M)'].unique())
print(unique_values)

# converting Wage to thousands
unique_wage = sorted(FIFA['Wage'].unique())
print(unique_wage)

# function to convert Wage to values in thousands ()

def convert_to_thousand(wage_str):
        # Check if the input is a string 
        if isinstance(wage_str, str):
            if 'K' in wage_str:
                # Remove '€' and 'K' and convert to float
                wage = float(wage_str.replace('€', '').replace('K', ''))
                return round(wage)
            else: 
                wage = float(wage_str.replace('€', ''))
                return wage  # Handle unexpected formats
        else:
            # Input is already a float, return it as is
            return wage_str
        
# apply the conversion function to the 'Wage' column
FIFA['Wage'] = FIFA['Wage'].apply(convert_to_thousand)
FIFA.rename(columns = {'Wage':'Wage(€K)'}, inplace = True)
FIFA['Wage(€K)'] = FIFA['Wage(€K)'].astype(float)  
unique_wage = sorted(FIFA['Wage(€K)'].unique())
print(unique_wage)       

# removing star symbol from W/F, SM and IR columns 
def remove_star(x):
    x = x.replace('★','')
    return x

FIFA['IR'] = FIFA['IR'].apply(remove_star)
FIFA['SM'] = FIFA['SM'].apply(remove_star)
FIFA['W/F'] = FIFA['W/F'].apply(remove_star)


# Visualize Relationships
# importing necessary modules


import seaborn as sns
import matplotlib.pyplot as plt

# Create a joint plot to visualize the relationship between Age and Overall Rating (OVA)
plot = sns.jointplot(data=FIFA, x='Age', y='OVA', hue='Preferred Foot')

# Display the joint plot
plt.show()

# Filter and display player information for those with Age 53
filtered_players_age_53 = FIFA.loc[FIFA['Age'] == 53, ['FullName', 'Nationality', 'Club']]

# Display the distribution of Overall Ratings (OVA) for all players
plt.figure(figsize=(10, 10))
plt.title("Overall Rating Analysis")
plt.hist(FIFA['OVA'], bins=[40, 50, 60, 70, 80, 90, 100], color='plum', edgecolor='black')
plt.show()

# Calculate the frequency of players in different Overall Rating (OVA) ranges
ova_freq = [FIFA.query(f'{i} < OVA <= {i + 10}').shape[0] for i in range(40, 100, 10)]

# Display the Overall Rating (OVA) distribution using a pie chart
plt.figure(figsize=(20, 10))
plt.title("Overall Rating Range")
plt.pie(ova_freq, autopct='%.2f', labels=[f'{i} to {i + 10}' for i in range(40, 100, 10)])
plt.show()
