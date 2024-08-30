import pandas as pd
import matplotlib.pyplot as plt

ratings_file_path = 'ratings.csv'
movies_file_path = 'movies.csv'


ratings_df = pd.read_csv(ratings_file_path)
movies_df = pd.read_csv(movies_file_path)

print(ratings_df.head())
print(movies_df.head())

top_movies = ratings_df.groupby('movieId')['rating'].count().sort_values(ascending=False).head(11)
top_movies = top_movies.reset_index().merge(movies_df[['movieId', 'title']], on='movieId', how='left')

print(top_movies)

plt.figure(figsize=(10, 6))
plt.barh(top_movies['title'], top_movies['rating'], color='blue')
plt.xlabel('Puan Sayisi')
plt.ylabel('Film ismi')
plt.title('En Çok Puan Alan Filmler')
plt.gca().invert_yaxis()  #y ekseniters 
plt.show()




