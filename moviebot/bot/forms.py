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

class MovieForm(forms.Form):
    movie = forms.ChoiceField(get_movie_names)



