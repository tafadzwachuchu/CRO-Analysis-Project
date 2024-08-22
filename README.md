Python Code Description
1. Data Cleaning and Visualization for Three Sites
This Python script is designed to clean and preprocess raw data from three different web pages (Home Page, Cart Exit, and Post-Purchase). The cleaning process involves handling missing values, correcting data types, and removing duplicates to ensure the dataset is ready for analysis.

Key Steps:

Loading Data: The script imports the raw data files for each of the three pages.
Data Cleaning:
Missing values are handled by either imputing them or removing rows/columns with excessive missing data.
Data types are corrected to ensure proper numeric, categorical, or datetime formats.
Duplicate entries are identified and removed to avoid skewed analysis.
Feature Engineering: New features are created to provide additional insights during the analysis phase.
Visualization:
The cleaned data is visualized using Python libraries such as Matplotlib and Seaborn.
The script generates key visualizations that help identify trends and patterns across each of the three pages.
Outputs:

A series of visualizations including bar charts, line graphs, and scatter plots that summarize the cleaned data.
These visuals are designed to provide insights into user behavior on each of the three pages, highlighting areas for potential optimization.
2. Data Cleaning and Creation of New Files
This Python script is focused on the comprehensive cleaning of the dataset followed by the creation of new, clean data files for each of the three pages.

Key Steps:

Loading Data: The script begins by loading the raw data from local files.
Data Cleaning:
Handles missing data by applying appropriate methods such as filling with mean/median values or dropping null entries.
Standardizes data formats, ensuring consistency across the dataset.
Removes any outliers that could distort analysis results.
Renames columns for better clarity and consistency.
File Creation:
Once cleaned, the script saves the processed data into new Excel files, one for each of the three pages (Home Page, Cart Exit, Post-Purchase).
These files are then ready to be imported into visualization tools like Power BI for further analysis.
Outputs:

Cleaned data files for each page saved in Excel format (.xlsx), ensuring they are ready for visualization and analysis.
Each file reflects the structured, error-free data necessary for reliable insights.
