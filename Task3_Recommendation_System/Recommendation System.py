# Task 4 - Recommendation System

# Movie database
movies = [
    {"name": "Avengers: Endgame", "genre": "action"},
    {"name": "Spider-Man: No Way Home", "genre": "action"},
    {"name": "The Dark Knight", "genre": "action"},
    {"name": "Interstellar", "genre": "sci-fi"},
    {"name": "Inception", "genre": "sci-fi"},
    {"name": "The Martian", "genre": "sci-fi"},
    {"name": "The Notebook", "genre": "romance"},
    {"name": "Titanic", "genre": "romance"},
    {"name": "La La Land", "genre": "romance"},
    {"name": "3 Idiots", "genre": "comedy"},
    {"name": "Hera Pheri", "genre": "comedy"},
    {"name": "Welcome", "genre": "comedy"}
]

print("======================================")
print("       MOVIE RECOMMENDATION SYSTEM")
print("======================================")

print("\nAvailable Genres:")
print("Action")
print("Sci-Fi")
print("Romance")
print("Comedy")

# Take user's preference
preference = input("\nEnter your favorite genre: ").lower()

# Find matching movies
recommendations = []

for movie in movies:
    if movie["genre"] == preference:
        recommendations.append(movie["name"])

# Display recommendations
if recommendations:
    print("\nRecommended Movies:")
    
    for movie in recommendations:
        print("-", movie)
else:
    print("\nSorry, no movies found for this genre.")

print("\nThank you for using the Movie Recommendation System!")