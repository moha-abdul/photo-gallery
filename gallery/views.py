from django.http  import HttpResponse
from django.shortcuts import render, redirect
from .models import Photos, Category, Location

# def hello(request):
#     return HttpResponse('Welcome to my photo gallery')

def all_photos(request):

    photos = Photos.objects.all()
    categories = Category.objects.all()
    locations = Location.objects.all()
    return render(request, 'all-photos/photos.html', {'photos' : photos,"categories": categories, "locations": locations})

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
        name = request.GET.get("photo")
        searched_categories = Photos.search_by_category(name)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"photos": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

def filter_by_location(request, location):
    images = Location.objects.get(name=location)
    photos = Photos.objects.filter(location_id=images.id)

    return render(request, 'all-photos/locations.html', {"images" : photos})
   
# def nav(request):
#     locations = Location.objects.all()
#     return render('navbar.html',{"locations":locations})