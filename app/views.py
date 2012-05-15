# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def render_response(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)

def synopsis(request):
    return render_response(request, 'synopsis.html', {  })

def movie(request):
   return render_response(request, 'movie.html', {  })

def gallery(request):
    image_index = [ 1,2,3,4,5,6,7,8,9,10,11,12,13]
    return render_response(request, 'gallery.html', { 'image_index' : image_index })
def director(request):
    return render_response(request, 'director.html', {  })

def contact(request):
    return render_response(request, 'contact.html', {  })
