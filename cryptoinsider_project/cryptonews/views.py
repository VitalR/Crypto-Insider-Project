import json
import requests

from django.shortcuts import render


def home(request):
    news_api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    news_api = json.loads(news_api_request.content)
    return render(request, 'cryptonews/home.html', {'news_api': news_api})
