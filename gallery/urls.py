from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.hello,name = 'hello'),
    # url('^all-photos/$',views.all_photos,name='photos')
]