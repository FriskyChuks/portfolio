from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    # path('contact/',contact,name='contact'),
    # path('services/',services,name='services'),
    # path('about_us/',about_us,name='about_us'),
    # path('works/',works,name='works'),
]
