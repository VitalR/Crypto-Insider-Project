from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_coin, name='search_coin'),
    path('news/', views.news, name='news'),
    path('prices/', views.prices, name='prices'),
    path('crypto_basics/', views.crypto_basics, name='crypto_basics'),
    # path('crypto_basics/article/', views.crypto_article, name='crypto_article'),

]
