from django.urls import path

from karobar import views

urlpatterns = [
    path('', views.index, name='index'),
]
