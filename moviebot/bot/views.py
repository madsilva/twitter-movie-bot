from django.shortcuts import render
from .forms import TwitterUserForm

def index(request):
    context = {}
    if ('submit' in request.GET):
        user = request.GET['twitter_user']
        context['twitter_user'] = user
        context['form'] = TwitterUserForm(request.GET)
        context['user_image_url'] = "https://twitter.com/" + user + "/profile_image?size=original"
        context['graph_url'] = "static/bot/" + user + ".jpg"
        # do something with user to get image
    else:
        context['form'] = TwitterUserForm()
    return render(request, "bot/index.html", context)
