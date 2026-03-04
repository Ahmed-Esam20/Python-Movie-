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


# =========================================================
# 8) Count movies for each individual genre
# =========================================================
genres_split = df.assign(genres=df["genres"].str.split(",")).explode("genres")
genres_split["genres"] = genres_split["genres"].str.strip()

genre_counts = genres_split["genres"].value_counts()

print("\nMovies per genre:")
print(genre_counts.head(10))


# =========================================================
# 9) Compare average rating long vs short movies (>120 min)
# =========================================================
# df["length_category"] = df["runtime"].apply(lambda x: "Long" if x > 120 else "Short")

# length_comparison = df.groupby("length_category")["tomatometer_rating"].mean()

# print("\nLong vs Short movies rating:")
# print(length_comparison)


# =========================================================
# 10) Top-rated movie per genre
# =========================================================
top_per_genre = genres_split.sort_values(
    "tomatometer_rating", ascending=False
).drop_duplicates("genres")[["genres", "movie_title", "tomatometer_rating"]]

print("\nTop movie per genre:")
print(top_per_genre.head(10))

