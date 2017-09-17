from django import forms
import tmdbsimple as tmdb
tmdb.API_KEY = "6333e6cd17516cd6c57fcb2a4f0e4fe6"


def get_movie_names():
    movies = tmdb.Movies()
    now_playing_dict = movies.now_playing()['results']
    now_playing_list = []
    for movie in now_playing_dict:
        now_playing_list.append((movie['id'], movie['title']))
    return now_playing_list

class NowPlayingMovieForm(forms.Form):
    movie = forms.ChoiceField(get_movie_names)

def get_pop_names():
    movies = tmdb.Movies()
    pop_dict = movies.popular()['results']
    pop_list = []
    for movie in pop_dict:
        pop_list.append((movie['id'], movie['title']))
    return pop_list

class PopularMovieForm(forms.Form):
    movie = forms.ChoiceField(get_pop_names)



