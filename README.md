# FIFA 2021 Data Analysis
## Overview
This project involves analyzing FIFA 2021 player data to gain insights and perform data cleaning, transformation, and visualization. The goal is to prepare the dataset for further analysis and generate meaningful visualizations.
## Dataset
Dataset Source: Kaggle - <br>
https://www.kaggle.com/datasets/yagunnersya/fifa-21-messy-raw-dataset-for-cleaning-exploring?select=fifa21_raw_data.csv%E2%80%8B <br> <br>
The dataset consists of FIFA 2021 players features such as Name, Club, OVA, Value etc. Data is in different formats, raw and messy.

#   Column            Non-Null Count  Dtype 
---  ------            --------------  ----- 
 0   ID                18979 non-null  int64 
 1   Name              18979 non-null  object
 2   LongName          18979 non-null  object
 3   photoUrl          18979 non-null  object
 4   playerUrl         18979 non-null  object
 5   Nationality       18979 non-null  object
 6   Age               18979 non-null  int64 
 7   ↓OVA              18979 non-null  int64 
 8   POT               18979 non-null  int64 
 9   Club              18979 non-null  object
 10  Contract          18979 non-null  object
 11  Positions         18979 non-null  object
 12  Height            18979 non-null  object
 13  Weight            18979 non-null  object
 14  Preferred Foot    18979 non-null  object
 15  BOV               18979 non-null  int64 
 16  Best Position     18979 non-null  object
 17  Joined            18979 non-null  object
 18  Loan Date End     1013 non-null   object
 19  Value             18979 non-null  object
 20  Wage              18979 non-null  object
 21  Release Clause    18979 non-null  object
 22  Attacking         18979 non-null  int64 
 23  Crossing          18979 non-null  int64 
 24  Finishing         18979 non-null  int64 
 25  Heading Accuracy  18979 non-null  int64 
 26  Short Passing     18979 non-null  int64 
 27  Volleys           18979 non-null  int64 
 28  Skill             18979 non-null  int64 
 29  Dribbling         18979 non-null  int64 
 30  Curve             18979 non-null  int64 
 31  FK Accuracy       18979 non-null  int64 
 32  Long Passing      18979 non-null  int64 
 33  Ball Control      18979 non-null  int64 
 34  Movement          18979 non-null  int64 
 35  Acceleration      18979 non-null  int64 
 36  Sprint Speed      18979 non-null  int64 
 37  Agility           18979 non-null  int64 
 38  Reactions         18979 non-null  int64 
 39  Balance           18979 non-null  int64 
 40  Power             18979 non-null  int64 
 41  Shot Power        18979 non-null  int64 
 42  Jumping           18979 non-null  int64 
 43  Stamina           18979 non-null  int64 
 44  Strength          18979 non-null  int64 
 45  Long Shots        18979 non-null  int64 
 46  Mentality         18979 non-null  int64 
 47  Aggression        18979 non-null  int64 
 48  Interceptions     18979 non-null  int64 
 49  Positioning       18979 non-null  int64 
 50  Vision            18979 non-null  int64 
 51  Penalties         18979 non-null  int64 
 52  Composure         18979 non-null  int64 
 53  Defending         18979 non-null  int64 
 54  Marking           18979 non-null  int64 
 55  Standing Tackle   18979 non-null  int64 
 56  Sliding Tackle    18979 non-null  int64 
 57  Goalkeeping       18979 non-null  int64 
 58  GK Diving         18979 non-null  int64 
 59  GK Handling       18979 non-null  int64 
 60  GK Kicking        18979 non-null  int64 
 61  GK Positioning    18979 non-null  int64 
 62  GK Reflexes       18979 non-null  int64 
 63  Total Stats       18979 non-null  int64 
 64  Base Stats        18979 non-null  int64 
 65  W/F               18979 non-null  object
 66  SM                18979 non-null  object
 67  A/W               18979 non-null  object
 68  D/W               18979 non-null  object
 69  IR                18979 non-null  object
 70  PAC               18979 non-null  int64 
 71  SHO               18979 non-null  int64 
 72  PAS               18979 non-null  int64 
 73  DRI               18979 non-null  int64 
 74  DEF               18979 non-null  int64 
 75  PHY               18979 non-null  int64 
 76  Hits              16384 non-null  object

## Project Structure
### 1. Data Import and Cleaning
- Imported FIFA player data from a zip file.
- Checked and explored the dataset using various methods such as: .head, .tail, .info, .shape, .describe, to better understand the dataset and be able to take insightfull actions. 
- Dropped unnecessary columns, that are not useful for analysis.
- Renamed columns for clarity.
- Filled null values in the 'Hits' column with zeros, leaving null values could disrupt activities on this column.
- Cleaned the 'Club' column from '\n\n\n\n' values. 
### 2. Data Transformation
- Converted the 'Joined' column to a proper date-time format, from 'Jul 1, 2004' to '2004-07-01'
- Converted the 'Height' column to centimeters.
- Converted the 'Weight' column to kilograms.
- Converted 'Value' to values in millions.
- Converted 'Wage' to values in thousands.
- Removed star symbols from 'W/F,' 'SM,' and 'IR' columns.
### 3. Data Visualization
- Created a joint plot to visualize the relationship between Age and Overall Rating (OVA), with additional breakdown on righ or left foot. <br><br>
  ![image](https://github.com/Mazur-Piotr/FIFA2021_Data_Cleaning-Portfolio_Project/assets/138219323/65419315-0df6-4037-b128-376730bd59b0)
<br>

- Displayed the distribution of Overall Ratings (OVA) for all players using a histogram. <br><br>

![image](https://github.com/Mazur-Piotr/FIFA2021_Data_Cleaning-Portfolio_Project/assets/138219323/6ced9a39-642d-48fb-9905-18cecfb34034)

<br>  

- Calculated the frequency of players in different Overall Rating (OVA) ranges and visualized it with a pie chart. <br>

![image](https://github.com/Mazur-Piotr/FIFA2021_Data_Cleaning-Portfolio_Project/assets/138219323/34bdfd53-b8bf-4b23-a0ae-8237222044ca)

<br>

## Technologies Used
- Python: Pandas, Matplotlib, Seaborn

### Usage
This project provides a comprehensive analysis of FIFA 2021 player data and can serve as a foundation for more advanced data analysis tasks and insights.

### Credits
This project was created by Piotr on September 21, 2023.
