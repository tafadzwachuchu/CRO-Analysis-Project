import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'homepage.xlsx'  # Update this with your actual file path
df = pd.read_excel(file_path)

# Display the first few rows and column names
print("First few rows of the dataframe:")
print(df.head())
print("\nColumn Names:")
print(df.columns)

# Fill missing values with 'Not Specified' for relevant columns
df['What is most important for you right now?'].fillna('Not Specified', inplace=True)
df['What are you looking for from PowerDot\'s website today?'].fillna('Not Specified', inplace=True)
df['How did you FIRST hear about us?'].fillna('Not Specified', inplace=True)
df['How old are you?'].fillna('Not Specified', inplace=True)
df['What is your gender?'].fillna('Not Specified', inplace=True)
df['Device'].fillna('Not Specified', inplace=True)
df['Country'].fillna('Not Specified', inplace=True)
