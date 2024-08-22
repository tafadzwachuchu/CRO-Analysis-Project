import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from Excel
file_path = 'cart.xlsx'
df = pd.read_excel(file_path)

# Display the first few rows and column names for verification
print("First few rows of the dataframe:")
print(df.head())
print("\nColumn Names:")
print(df.columns)

# Handle missing values for relevant columns
df['Quick question for you: How did you FIRST hear about us?'].fillna('Not Specified', inplace=True)
df['When did you FIRST hear about us?'].fillna('Not Specified', inplace=True)
df['Final question: Briefly, what nearly stopped you from buying from us?'].fillna('Not Specified', inplace=True)

# Prepare data for plotting
hear_about_counts = df['Quick question for you: How did you FIRST hear about us?'].value_counts()
hear_about_time_counts = df['When did you FIRST hear about us?'].value_counts()
stopped_counts = df['Final question: Briefly, what nearly stopped you from buying from us?'].value_counts()

# Create a dashboard-like layout
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(14, 18))
fig.tight_layout(pad=6.0)

# Plot 1: How Did You FIRST Hear About Us?
sns.barplot(x=hear_about_counts.index, y=hear_about_counts.values, palette='viridis', ax=axes[0])
axes[0].set_title('How Did You FIRST Hear About Us?')
axes[0].set_xlabel('Source')
axes[0].set_ylabel('Number of Responses')
axes[0].tick_params(axis='x', rotation=45)

# Plot 2: When Did You FIRST Hear About Us?
sns.barplot(x=hear_about_time_counts.index, y=hear_about_time_counts.values, palette='coolwarm', ax=axes[1])
axes[1].set_title('When Did You FIRST Hear About Us?')
axes[1].set_xlabel('Time')
axes[1].set_ylabel('Number of Responses')
axes[1].tick_params(axis='x', rotation=45)

# Plot 3: What Nearly Stopped You From Buying?
sns.barplot(x=stopped_counts.index, y=stopped_counts.values, palette='pastel', ax=axes[2])
axes[2].set_title('What Nearly Stopped You From Buying?')
axes[2].set_xlabel('Reason')
axes[2].set_ylabel('Number of Responses')
axes[2].tick_params(axis='x', rotation=45)

# Show the combined dashboard
plt.show()
