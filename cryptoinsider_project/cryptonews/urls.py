from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_coin, name='search_coin'),
    path('news/', views.news, name='news'),
    path('prices/', views.prices, name='prices'),

]
