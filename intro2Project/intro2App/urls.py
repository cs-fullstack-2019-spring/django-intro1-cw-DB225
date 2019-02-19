from django.urls import path

from . import views

# Paths for each artist inside the music request
urlpatterns = [
    path('', views.index, name='index'),
    path('music/', views.music, name='index'),
    path('music/Jimmy_Hendrix/', views.Jimmy_Hendrix, name='index'),
    path('music/Elton_John/', views.Elton_John, name='index'),
    path('music/Michael_Jackson/', views.Michael_Jackson, name='index'),
]