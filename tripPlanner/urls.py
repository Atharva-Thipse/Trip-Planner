from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('place',views.places,name='place'),
    path('add',views.add,name='add'),
]
