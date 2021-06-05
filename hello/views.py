from pprint import pprint
from django.shortcuts import render
from pymongo import MongoClient, ASCENDING

mongoUrl = ""


def page_home(request):
    client = MongoClient(port=27017)
    db = client.music

    result = db.albums.find(
        {},
        {
            "alb_nom": 1,
            "alb_artiste.art_nom": 1,
            "alb_prix": 1
        }).sort(
        [
            ("alb_prix", ASCENDING),
            ("alb_nom", ASCENDING)
        ])

    return render(request, 'hello/home.html', {
        'albums': result
    })
