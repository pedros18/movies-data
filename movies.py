import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Load the CSV file
file_path = '/home/badreddine/Downloads/movies_metadata.csv'
movies_data = pd.read_csv(file_path)

# Convert release_date to datetime
movies_data['release_date'] = pd.to_datetime(movies_data['release_date'], errors='coerce')

# Extract year from release_date
movies_data['release_year'] = movies_data['release_date'].dt.year

# Plot 1: Distribution of Movie Ratings
plt.figure(figsize=(10, 6))
sns.histplot(movies_data['vote_average'].dropna(), bins=30, kde=True)
plt.title('Distribution of Movie Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Movies')
plt.show()

# Plot 2: Number of Movies Released Each Year
plt.figure(figsize=(10, 6))
movies_per_year = movies_data['release_year'].dropna().value_counts().sort_index()
sns.lineplot(x=movies_per_year.index, y=movies_per_year.values)
plt.title('Number of Movies Released Each Year')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.show()

# Plot 3: Top 10 Most Common Genres
import ast

# Expand the genres column
movies_data['genres'] = movies_data['genres'].dropna().apply(ast.literal_eval)
movies_data['genres'] = movies_data['genres'].apply(lambda x: [d['name'] for d in x] if isinstance(x, list) else [])

# Explode the genres into separate rows
all_genres = movies_data.explode('genres')
top_genres = all_genres['genres'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_genres.values, y=top_genres.index)
plt.title('Top 10 Most Common Genres')
plt.xlabel('Number of Movies')
plt.ylabel('Genre')
plt.show()

# Plot 4: Correlation Between Budget and Revenue
plt.figure(figsize=(10, 6))
# Convert budget and revenue to numeric, forcing errors to NaN
movies_data['budget'] = pd.to_numeric(movies_data['budget'], errors='coerce')
movies_data['revenue'] = pd.to_numeric(movies_data['revenue'], errors='coerce')
sns.scatterplot(x='budget', y='revenue', data=movies_data)
plt.title('Correlation Between Budget and Revenue')
plt.xlabel('Budget')
plt.ylabel('Revenue')
plt.xscale('log')
plt.yscale('log')
plt.show()

