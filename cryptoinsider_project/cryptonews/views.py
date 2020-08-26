import json
import requests

from django.shortcuts import render


def home(request):
    price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP&tsyms=USD')
    price = json.loads(price_request.content)


    news_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    news = json.loads(news_request.content)

    return render(request, 'cryptonews/home.html', {'news': news, 'price': price})
