import pandas as pd

# Define file paths
post_file = 'post.xlsx'
homepage_file = 'homepage.xlsx'
cart_file = 'cart.xlsx'

# Load datasets
post_df = pd.read_excel(post_file)
homepage_df = pd.read_excel(homepage_file)
cart_df = pd.read_excel(cart_file)

# Clean Post-Purchase Data
post_df['Quick question for you: How did you FIRST hear about us?'].fillna('Not Specified', inplace=True)
post_df['When did you FIRST hear about us?'].fillna('Not Specified', inplace=True)
post_df['Final question: Briefly, what nearly stopped you from buying from us?'].fillna('Not Specified', inplace=True)

# Save cleaned post-purchase data
post_df.to_excel('cleaned_post.xlsx', index=False)

# Clean Homepage Data
homepage_df['What is most important for you right now?'].fillna('Not Specified', inplace=True)
homepage_df['What are you looking for from PowerDot\'s website today?'].fillna('Not Specified', inplace=True)
homepage_df['How did you FIRST hear about us?'].fillna('Not Specified', inplace=True)
homepage_df['How old are you?'].fillna('Not Specified', inplace=True)
homepage_df['What is your gender?'].fillna('Not Specified', inplace=True)

# Save cleaned homepage data
homepage_df.to_excel('cleaned_homepage.xlsx', index=False)

# Clean Cart Data
# Adjust columns based on your actual cart data structure
required_cart_columns = ['Device', 'Country']
for col in required_cart_columns:
    if col not in cart_df.columns:
        raise ValueError(f"Column '{col}' is missing from the cart dataset.")
    cart_df[col].fillna('Not Specified', inplace=True)

# Save cleaned cart data
cart_df.to_excel('cleaned_cart.xlsx', index=False)

print("Data cleaning completed. Cleaned files have been saved.")
