from django.shortcuts import render
from main.models import Item, ItemPhoto


def home(request):
    return render(request, 'main/index.html')


def buy(request):
    return render(request, 'main/how_to_bye.html')


def catalog(request):
    items = Item.objects.all()
    for item in items:
        item.img = ItemPhoto.objects.filter(item=item).values('image')

    data = {'items':items}

    return render(request, 'main/catalogue.html', context=data)
