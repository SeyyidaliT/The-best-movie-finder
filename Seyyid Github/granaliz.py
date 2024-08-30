import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Genresi kullan 
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')


movies['genres'] = movies['genres'].str.split('|')
genres = movies['genres'].explode().value_counts()

plt.figure(figsize=(12, 8))
sns.barplot(x=genres.values, y=genres.index)
plt.title('en cok tercih edilen kategoriler')
plt.xlabel('Film sayisi')
plt.ylabel('Kategori')
plt.show()
