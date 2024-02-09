#task1
from dict_of_movies import movies
def is_above_5_5(movies,movie_name):
    
    for movie in movies:
        if movie["name"].lower() == movie_name.lower():
            return movie["imdb"] > 5.5
        
user_input = input("Enter the name of the movie")
result = is_above_5_5(movies,user_input)
print(result)

#task2
from dict_of_movies import movies
def filter_above(movies):
    
    return[movie for movie in movies if movie["imdb"] > 5.5]
   
        
        
filtered_movies = filter_above(movies)
print(filtered_movies)

#task3
from dici_of_movies import movies
def filter_movies (movies,category):
    return[movie for movie in movies if movie["category"] == category]

category_name = input("Enter the name of category")
movies_in = filter_movies(movies, category_name)
if movies_in:
    print("Yes,it is in the same category")
else:
    print("No,they are not the same")

#task4
from dict_of_movies import movies
def calculate_average_imdb(movies):
    if not movies:
        return 0.0
    total_imdb = sum(movie["imdb"] for movie in movies)
    average_imdb = total_imdb / len(movies)
    return average_imdb

average_score = calculate_average_imdb(movies)
print(f"The average IMDB score of the movies is: {average_score}")

#task5
from dict_of_movies import movies
def calculate_average_imdb_by_category(movies, category):
    category_movies = [movie for movie in movies if movie["category"] == category]
    total_imdb = sum(movie["imdb"] for movie in category_movies)
    average_imdb = total_imdb / len(category_movies)
    return average_imdb

category_name = input("Enter the name of the category: ")
average_score = calculate_average_imdb_by_category(movies, category_name)
print(average_score)