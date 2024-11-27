from django.shortcuts import render
from main.models import Item

def home(request):
    return render(request, 'main/index.html')


def buy(request):
    return render(request, 'main/how_to_bye.html')


def catalog(request):
    data = {'candles': Item.objects.all()}
    return render(request, 'main/catalogue.html', context=data)