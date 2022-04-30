from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "name": "austin",
        "favorite_color": "red",
        "pets": ["tonail", "gabe", "Sir Squash"]
    }
    return render(request, "index.html", context)
    #return HttpResponse("this is the equivalent of @app.routes('/')")