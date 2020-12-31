import json
import requests

from django.shortcuts import render


def home(request):
    price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP&tsyms=USD')
    price = json.loads(price_request.content)

    news_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    news = json.loads(news_request.content)

    return render(request, 'cryptonews/home.html', {'news': news, 'price': price})


def search_coin(request):
    if request.method == 'POST':
        coin = request.POST['coin']
        price_request = requests.get(
            'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + coin + '&tsyms=USD')
        price = json.loads(price_request.content)
        return render(request, 'cryptonews/search_coin.html', {'coin': coin, 'price': price})
    else:
        return render(request, 'cryptonews/search_coin.html')


def news(request):
    news_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    news = json.loads(news_request.content)
    return render(request, 'cryptonews/news.html', {'news': news})


def prices(request):
    price_request = requests.get(
        'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,USDT,LINK,DOT,BCH,LTC,BSV,BNB,ADA,EOS,XTZ,XLM,TRX,XMR,USDC,NEO,VET,MIOTA,DASH,ETC,ZEC,LEND,ICX,WAVES,MKR,YFI&tsyms=USD')
    price = json.loads(price_request.content)

    return render(request, 'cryptonews/prices.html', {'price': price})


def crypto_basics(request):
    return render(request, 'cryptonews/crypto_basics.html')


# def crypto_article(request):
#     return render(request, '')