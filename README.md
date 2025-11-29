Quantitative Analysis of Saudi Domestic Tourism (2023)

This mini-project analyzes domestic tourism trends in Saudi Arabia using real-world data from the Saudi Open Data Portal. The project applies essential data science techniques including data cleaning, exploratory data analysis (EDA), visualization, and a simple linear regression model to study the relationship between monthly tourist numbers and tourism spending.

Dataset

Source: Saudi Open Data Portal
Dataset: Domestic Tourists Number and Spending by Destination (2023)


The original dataset can be downloaded from the Saudi Open Data Portal:
https://portal.opendata.sa/dataset/xxxx

Variables used:
-Total number of domestic tourists per month
-Total monthly tourism spending

The dataset originally contained additional metadata and regional columns, which were removed during preprocessing.

Data Cleaning and Preparation

Key steps performed include:
-Handling missing values using forward-fill
-Removing irrelevant metadata columns
-Filtering meaningful indicators only
-Converting text fields to numeric values
-Merging tourist and spending subsets into a unified dataframe
-Producing a clean dataset with 12 monthly records

Exploratory Data Analysis (EDA)

The analysis includes:
-Descriptive statistics (mean, median, minimum, maximum)
-Monthly trend analysis
-Line charts and bar charts
-Exploration of the relationship between tourist numbers and spending


Regression Model

A simple linear regression model was applied to evaluate the relationship between tourist numbers (independent variable) and tourism spending (dependent variable).

Model results:
-R² Score: 0.994
-Interpretation: A very strong positive linear relationship, indicating that tourism spending increases consistently as the number of tourists increases.


Technologies Used
-Python
-Pandas
-Matplotlib
-scikit-learn


How to Run the Project
1.Install the required libraries:
pip install pandas matplotlib scikit-learn

2.Run the analysis script:
python miniProject.py

Make sure the dataset path in the script matches your local directory.


Visualizations

All plots and charts used in this project are included in the Visualizations section of the final report. These include monthly tourist counts, monthly spending, regression scatter plot with line, and a combined trend chart.


Author

Ala Hussain Fahaid Alsagoor
