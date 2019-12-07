from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import *

from Airbus.helpers import populate
from Airbus.models.Feed import Feed


def posts(request):
    news = Feed.objects.using('news').all()
    page = request.GET.get('page', 1)
    paginator = Paginator(news, 10)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    return render(request, 'news.html', {'news': news})


def test_scroll(request):
    numbers_list = range(1, 1000)
    page = request.GET.get('page', 1)
    paginator = Paginator(numbers_list, 20)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'scroll.html', {'numbers': numbers})


def populate_posts(request):
    populate()
