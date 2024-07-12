
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='url-home' ),
    path('login/', views.logIndex, name= 'url-log'),
    path('cadastro/', views.cadIndex, name= 'url-cad'),
    path('inicio/', views.startIndex, name= 'url-start'),
    path('ajuda/', views.helpIndex, name='url-help'),
    path('classe/', views.classIndex, name='url-class'),
]