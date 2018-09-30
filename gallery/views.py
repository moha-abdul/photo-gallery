from django.http  import HttpResponse
from django.shortcuts import render, redirect
from .models import Photos, Category, Location


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





def filter_by_location(request, location):
    images = Location.objects.get(name=location)
    photos = Photos.objects.filter(location_id=images.id)

    return render(request, 'all-photos/locations.html', {"images" : photos})

def filter_by_category(request, category):
    images = Category.objects.get(name=category)
    photos = Photos.objects.filter(category_id=images.id)

    return render(request, 'all-photos/categories.html', {"images" : photos})
