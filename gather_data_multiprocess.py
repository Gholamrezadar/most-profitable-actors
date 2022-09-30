import csv
from collections import defaultdict
from dotenv import load_dotenv
import os
import requests
from multiprocessing import Pool

load_dotenv()
API_KEY = os.getenv('API_KEY')

def get_movie_id(movie_name, movie_year):
    """Gets the movie_id from TMDB using the movie_name and year

    Args:
        movie_name (str): Movie's name
        movie_year (str): Movie's release year

    Returns:
        int: Movie TMDB id
    """

    try:
        r = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=en-US&page=1&include_adult=false', params={'query':movie_name, 'year':movie_year})
        movie_id = r.json()['results'][0]['id']
        return movie_id
    except:
        return 100

def get_movie_actors(movie_name, movie_year, limit=20):
    """Returns the top 'limit' movie actors

    Args:
        movie_name (str): Movie's name
        movie_year (str): Movie's release year
        limit (int, optional): Actors limit. Defaults to 20.

    Returns:
        str[]: A list of movie actors
    """

    actors = []

    movie_id = get_movie_id(movie_name, movie_year)
    r = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}&language=en-US&')

    actors_json = r.json()['cast'][:limit]
    for actor in actors_json:
        actors.append(actor['name'])

    return actors


def get_movie_actors_wrapper(movie_detail):
    return get_movie_actors(movie_detail[1], movie_detail[2], limit=20)

import pickle

def pickling(path, data):
    file = open(path,'wb')
    pickle.dump(data,file)

def unpickling(path):
    file = open(path, 'rb')
    b = pickle.load(file)
    return b

if __name__ == '__main__':

    # get movies name and year from csv
    movies_list = []
    with open('top_movies_list.csv', newline='') as file:
        reader = csv.reader(file)
        for idx, movie in enumerate(reader):
            movies_list.append(movie)
            
    # get movie actors multiprocessing
    with Pool(55) as p:
            data = p.map(get_movie_actors_wrapper, movies_list)
            pickling("data.pckl", data)
