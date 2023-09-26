# FIFA 2021 Data Analysis
## Overview
This project involves analyzing FIFA 2021 player data to gain insights and perform data cleaning, transformation, and visualization. The goal is to prepare the dataset for further analysis and generate meaningful visualizations.
## Dataset
Dataset Source: Kaggle - <br>
https://www.kaggle.com/datasets/yagunnersya/fifa-21-messy-raw-dataset-for-cleaning-exploring?select=fifa21_raw_data.csv%E2%80%8B <br> <br>
The dataset consists of FIFA 2021 players features such as Name, Club, OVA, Value etc. Data is in different formats, raw and messy.

## Project Structure
### 1. Data Import and Cleaning
- Imported FIFA player data from a zip file.
- Checked and explored the dataset.
- Dropped unnecessary columns.
- Renamed columns for clarity.
- Filled null values in the 'Hits' column with zeros.
- Cleaned the 'Club' column from '\n\n\n\n' values.
### 2. Data Transformation
- Converted the 'Joined' column to a proper date-time format.
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
