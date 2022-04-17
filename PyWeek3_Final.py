#Q1 - fetch data from tastedrive (documentation at https://tastedive.com/read/api)

import requests_with_caching
import json
def get_movies_from_tastedive(string):
    base_url="https://tastedive.com/api/similar"
    params_diction = {}
    params_diction['q']=string
    params_diction['type']='movies'
    params_diction['limit']=5
    tastedive_response = requests_with_caching.get(base_url, params = params_diction)
    print(tastedive_response.url)
    return tastedive_response.json()


#Q2 - unction that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive. Call it extract_movie_titles
import requests_with_caching
import json
def get_movies_from_tastedive(string):
    base_url="https://tastedive.com/api/similar"
    params_diction = {}
    params_diction['q']=string
    params_diction['type']='movies'
    params_diction['limit']=5
    tastedive_response = requests_with_caching.get(base_url, params = params_diction)
    print(tastedive_response.url)
    return tastedive_response.json()

def extract_movie_titles(result):
    dic=result['Similar']
    l=len(dic['Results'])
    li=[]
    for i in range(l):
        li.append(dic['Results'][i]['Name'])
    return li
 
#Q3 - function, called get_related_titles. It takes a list of movie titles as input. It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list. Don’t include the same movie twice.

import requests_with_caching
import json
def get_movies_from_tastedive(string):
    base_url="https://tastedive.com/api/similar"
    params_diction = {}
    params_diction['q']=string
    params_diction['type']='movies'
    params_diction['limit']=5
    tastedive_response = requests_with_caching.get(base_url, params = params_diction)
    print(tastedive_response.url)
    return tastedive_response.json()

def extract_movie_titles(result):
    dic=result['Similar']
    l=len(dic['Results'])
    li=[]
    for i in range(l):
        li.append(dic['Results'][i]['Name'])
    return li

def get_related_titles(movie_lis):
    li=[]
    for movie in movie_lis:
        li.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(li))

#Q4 - https://www.omdbapi.com/, Define a function called get_movie_data. It takes in one parameter which is a string that should represent the title of a movie you want to search. The function should return a dictionary with information about that movie.

import requests_with_caching
import json

def get_movie_data(title):
    base_url = 'http://www.omdbapi.com/'
    params_diction = {}
    params_diction['t'] = title
    params_diction['r'] = 'json'
    this_page_cache = requests_with_caching.get(base_url, params=params_diction)

    return json.loads(this_page_cache.text)

#Q5 - function called get_movie_rating. It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer.

import requests_with_caching
import json


def get_movie_data(title):
    base_url = 'http://www.omdbapi.com/'
    params_diction = {}
    params_diction['t'] = title
    params_diction['r'] = 'json'
    this_page_cache = requests_with_caching.get(base_url, params=params_diction)

    return json.loads(this_page_cache.text)

def get_movie_rating(dic):
    rating = dic['Ratings']
    for item in rating:
        if item['Source'] == 'Rotten Tomatoes':
            return int(item['Value'][:-1])
    return 0

#Q6 - put it all together, Define a function get_sorted_recommendations. It takes a list of movie titles as an input. It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating function. Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.

import requests_with_caching
import json
def get_movies_from_tastedive(string):
    base_url="https://tastedive.com/api/similar"
    params_diction = {}
    params_diction['q']=string
    params_diction['type']='movies'
    params_diction['limit']=5
    tastedive_response = requests_with_caching.get(base_url, params = params_diction)
    #print(tastedive_response.url)
    return tastedive_response.json()

def extract_movie_titles(result):
    dic=result['Similar']
    l=len(dic['Results'])
    li=[]
    for i in range(5):
        li.append(dic['Results'][i]['Name'])
    return li

def get_related_titles(movie_lis):
    li=[]
    for movie in movie_lis:
        li.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(li))

def get_movie_data(title):
    base_url = 'http://www.omdbapi.com/'
    params_diction = {}
    params_diction['t'] = title
    params_diction['r'] = 'json'
    this_page_cache = requests_with_caching.get(base_url, params=params_diction)

    return json.loads(this_page_cache.text)

def get_movie_rating(dic):
    rating = dic['Ratings']
    for item in rating:
        if item['Source'] == 'Rotten Tomatoes':
            return int(item['Value'][:-1])
    return 0
   

def get_sorted_recommendations(listt):
    n_list = get_related_titles(listt)
    n_dict = {}
    for i in n_list:
        rating = get_movie_rating(get_movie_data(i))
        n_dict[i] = rating
    print(n_dict)
    print(sorted(n_dict, reverse=True))
    return [i[0] for i in sorted(n_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]

    