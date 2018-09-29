from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from gallery.views import all_photos, search_image

urlpatterns=[
    # url('^$',views.hello,name = 'hello'),
    url(r'^$',all_photos,name='all_photos'),
    url(r'^locations/(\w+)',views.filter_by_location, name = 'location'),
    url(r'^categories/(\w+)',views.filter_by_category, name = 'category'),
    url(r'^search/', views.search_image, name='search_image'),
    # url(r'^categories/', views.search_by_category, name='searching')
    # url(r'^article/(\d+)',views.article,name ='article')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)