from django.shortcuts import render
import tmdbsimple as tmdb
tmdb.API_KEY = "6333e6cd17516cd6c57fcb2a4f0e4fe6"

def index(request):
    movies = tmdb.Movies()
    now_playing_dict = movies.now_playing()['results']
    now_playing_list = []
    for movie in now_playing_dict:
        now_playing_list.append(movie['title'])
    return render(request, "bot/index.html", context={'now_playing_list':now_playing_list})
