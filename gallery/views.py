from django.http  import HttpResponse

# def hello(request):
#     return HttpResponse('Welcome to my photo gallery')

def all_photos(request):

    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    photos = Photo.all_photos()
    return render(request, 'all-photos/photos.html')
