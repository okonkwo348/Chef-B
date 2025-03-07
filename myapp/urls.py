from django.urls import path
from . import views  

urlpatterns=[
    path('home/',views.about, name='home'),
    path('menu/',views.menu, name='menu'),
    path('about/',views.about, name='about')
]