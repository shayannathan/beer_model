import pandas as pd

# Load Data
beer_file_path = './data/beer_reviews.csv'
beer_data = pd.read_csv(beer_file_path) 

# Data Cleaning
#print(beer_data.shape)
#print(beer_data.columns)
#print(beer_data.head())
#print(beer_data.isnull().sum()) # Check if there are missing values

# Feature Selection
beer_features = ['brewery_id', 'brewery_name', 'review_overall',
       'review_aroma', 'review_appearance', 'beer_style',
       'review_palate', 'review_taste', 'beer_name', 'beer_abv',
       'beer_beerid']

X = beer_data[beer_features]

print(X.head())
