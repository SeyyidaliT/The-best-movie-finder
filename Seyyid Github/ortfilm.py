import pandas as pd
import matplotlib.pyplot as plt


ratings_file_path = 'ratings.csv'
movies_file_path = 'movies.csv'

ratings_df = pd.read_csv(ratings_file_path)
movies_df = pd.read_csv(movies_file_path)


print(ratings_df.head())
print(movies_df.head())

# ortalama puani alan filmler
average_ratings = ratings_df.groupby('movieId')['rating'].mean().sort_values(ascending=False).head(11)
# Ortalama puanlarla basliklari birlestirme
average_ratings = average_ratings.reset_index().merge(movies_df[['movieId', 'title']], on='movieId', how='left')
print(average_ratings[['title', 'rating']])

plt.figure(figsize=(10, 6))
plt.barh(average_ratings['title'], average_ratings['rating'], color='orange')
plt.xlabel('Ortalama Puan')
plt.ylabel('Film İsmi')
plt.title('En Yüksek Ortalama Puan Alan Filmler')
plt.gca().invert_yaxis()  #?
plt.show()