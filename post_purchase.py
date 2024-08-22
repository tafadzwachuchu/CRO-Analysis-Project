import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'homepage_data.csv'  # Update this with your actual file path
df = pd.read_csv(file_path)

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

# Analyze "What is most important for you right now?"
importance_counts = df['What is most important for you right now?'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=importance_counts.index, y=importance_counts.values, palette='viridis')
plt.title('What is Most Important for Users Right Now?')
plt.xlabel('Importance')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Analyze "What are you looking for from PowerDot\'s website today?"
looking_for_counts = df['What are you looking for from PowerDot\'s website today?'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=looking_for_counts.index, y=looking_for_counts.values, palette='coolwarm')
plt.title('What Users Are Looking for from PowerDot\'s Website Today')
plt.xlabel('Looking For')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Analyze "How did you FIRST hear about us?"
first_heard_counts = df['How did you FIRST hear about us?'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=first_heard_counts.index, y=first_heard_counts.values, palette='pastel')
plt.title('How Users First Heard About Us')
plt.xlabel('Source')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Analyze "How old are you?"
age_counts = df['How old are you?'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=age_counts.index, y=age_counts.values, palette='plasma')
plt.title('Age Distribution of Users')
plt.xlabel('Age')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Analyze "What is your gender?"
gender_counts = df['What is your gender?'].value_counts()
plt.figure(figsize=(8, 6))
sns.barplot(x=gender_counts.index, y=gender_counts.values, palette='magma')
plt.title('Gender Distribution of Users')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Analyze "Device"
device_counts = df['Device'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=device_counts.index, y=device_counts.values, palette='cividis')
plt.title('Device Used by Users')
plt.xlabel('Device')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Analyze "Country"
country_counts = df['Country'].value_counts()
plt.figure(figsize=(12, 8))
sns.barplot(x=country_counts.index, y=country_counts.values, palette='mako')
plt.title('User Distribution by Country')
plt.xlabel('Country')
plt.ylabel('Count')
plt.xticks(rotation=90)  # Rotate x labels for better visibility
plt.tight_layout()
plt.show()
