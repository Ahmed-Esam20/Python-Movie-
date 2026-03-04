import pandas as pd

df = pd.read_csv("movies_cleaned_for_analysis.csv")

df["year"] = pd.to_datetime(df["original_release_date"], errors="coerce").dt.year

df["genres_list"] = df["genres"].str.split(",")

df["length_category"] = df["runtime"].apply(
    lambda x: "Long" if x > 120 else "Short"
)

df = df.drop_duplicates(subset="rotten_tomatoes_link")

df = df.dropna(subset=["tomatometer_rating", "genres", "year", "movie_title"])

# ============================================================================================================
# 1) Top 10 highest-rated movies
# =========================================================

top10 = df.sort_values(by="tomatometer_rating", ascending=False).head(10)
print(top10[["movie_title", "tomatometer_rating"]])



# =========================================================
# 2) Count of movies per genre
# =========================================================
genre_count = df["genres"].value_counts()

print("\nCount of movies per genres:")
print(genre_count)


# =========================================================
# 3) Filter movies released before 2000
# =========================================================

# df["original_release_date"] = pd.to_datetime(df["original_release_date"], errors="coerce")

# old_movies = df[df["original_release_date"].dt.year < 2000]

# print("\nMovies released before 2000:")
# print(old_movies[["movie_title", "original_release_date"]])

# =========================================================
# 4) Movies with rating above average
# =========================================================
avg_rating = df["tomatometer_rating"].mean()
above_avg_movies = df[df["tomatometer_rating"] > avg_rating]

print("\nMovies above average rating:")
print(above_avg_movies[["movie_title", "tomatometer_rating"]].head(10))


# =========================================================
# 5) Director with highest average rating
# =========================================================
director_avg = (
    df.groupby("directors")["tomatometer_rating"].mean().sort_values(ascending=False)
)

print("\nBest Director:")
print(director_avg.head(1))


# =========================================================
# 6) Count reviews > 100 characters
# =========================================================
print("\nTotal long reviews in dataset:")
print(df["long_reviews_count"].sum())


# =========================================================
# 7) Avg rating per year
# =========================================================
avg_per_year = df.groupby("year")["tomatometer_rating"].mean().sort_index()

print("\nAverage rating per year:")
print(avg_per_year.head(10))


