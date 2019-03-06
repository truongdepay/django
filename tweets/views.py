from django.shortcuts import render
from .models import Tweet

# Create your views here.

def tweet_detail_view(request, id = 1):

    return render(request, "tweets/detail_view.html", {})

def tweet_list_view(request):
    obj = Tweet.objects.all()
    print(obj)
    listItem = {
        'obj': obj
    }
    return render(request, "tweets/list_view.html", listItem)