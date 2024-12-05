from PIL.ImageTk import PhotoImage
from django.shortcuts import render
from main.models import Item, ItemPhoto

def home(request):
    return render(request, 'main/index.html')


def buy(request):
    return render(request, 'main/how_to_bye.html')


def catalog(request):
    item_ids = [num.id for num in Item.objects.all()]
    photos_item = ItemPhoto.objects.filter(item_id__in=item_ids)
    print(photos_item)
    #  TODO у каждого товара выводится его фото:
        #  TODO гуглить SQL group by
        #  TODO гуглить Django ORM group by
        #  TODO гуглить SQL left joint
        #  TODO гуглить Django ORM left joint
    data = {'candles': Item.objects.all(),
            'photos':photos_item }
    return render(request, 'main/catalogue.html', context=data)