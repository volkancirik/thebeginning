# Create your views here.
from django.shortcuts import render_to_response
def synopsis(request):
   return render_to_response("synopsis.html")
def movie(request):
   return render_to_response("movie.html")