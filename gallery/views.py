from django.http  import HttpResponse
from django.shortcuts import render, redirect
from .models import Photos, Category

# def hello(request):
#     return HttpResponse('Welcome to my photo gallery')

def all_photos(request):

    # photos = Photo.all_photos()
    photos = Photos.objects.all()
    return render(request, 'all-photos/photos.html', {'photos' : photos})

def search_image(request):
    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Photos.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})

def search_by_category(request):
    if 'photo' in request.GET and request.GET["photo"]:
        categories = Category.objects.all()
        return render(request, 'all-photos/search.html',{"categories": categories})

    else:
        message = "That category does not exist"
        return render(request, 'all-photos/search.html',{"message":message})