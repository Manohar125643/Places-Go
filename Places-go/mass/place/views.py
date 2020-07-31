from django.shortcuts import render
from django.http import HttpResponse
import requests, json

def font(request):
    return render(request,'back.html')


def home(request):
    return render(request,'home.html')


def add(request):
    api_key = 'ENTER_API_KEY'

    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    url2 = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    url3 = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=73945f078a6f0a904ce2d9e85645eeab'
    query= request.POST['num1']
    man = "places to visit in " + query
    r = requests.get(url + 'query=' + man +
                     '&key=' + api_key)
    x = r.json()
    y = x['results']
    r1 = requests.get(url2 + 'query=' + query +
                      '&key=' + api_key)

    x1 = r1.json()
    r2 = requests.get(url3.format(query)).json()

    y1 = x1['results']

    #mano={}
    #kano={}
    city_weather = {
        'city' : query,
        'temp' : r2['main']['temp'],
        'desc' : r2['weather'][0]['description'],
        'icon' : r2['weather'][0]['icon'],
    }

    result={}

    result.update({'city_weather': city_weather})

    for i in range(len(y1)):
        result.update({'lat': y1[i]['geometry']['location']['lat']})
        result.update({'lng': y1[i]['geometry']['location']['lng']})

    placesinfo = {}
    for i in range(len(y)):
        placesinfo.update({i: y[i]['name']})

    result.update({'placesinfo' : placesinfo})
    return render(request, "result.html",{'result':result})

