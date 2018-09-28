from django.http  import HttpResponse
from django.shortcuts import render, redirect
from .models import Photos

# def hello(request):
#     return HttpResponse('Welcome to my photo gallery')

def all_photos(request):

    # photos = Photo.all_photos()
    photos = Photos.objects.all()
    return render(request, 'all-photos/photos.html', {'photos' : photos})
