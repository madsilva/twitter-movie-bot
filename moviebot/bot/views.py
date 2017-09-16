from django.shortcuts import render

from .forms import MovieForm

import tmdbsimple as tmdb
tmdb.API_KEY = "6333e6cd17516cd6c57fcb2a4f0e4fe6"

def index(request):
    context = {}
    if request.GET['submit']:
        movie_id = request.GET['movie']
        movie = tmdb.Movies(movie_id)
        images = movie.images()
        image_filename = images['posters'][0]['file_path']
        image_url = "https://image.tmdb.org/t/p/original/" + image_filename
        context['image_url'] = image_url
    movie_form = MovieForm()
    context['movie_form'] = movie_form
    return render(request, "bot/index.html", context)
