from django.shortcuts import render
from django.contrib.gis.utils import GeoIP as g

def get_ip_address(request):
    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def about(request):
    context = {}
    return render(request, 'base/about.html', context)

def suprise(request):
    user_ip = get_ip_address(request)

    city_name = g.city(user_ip)['city']
    city_info = g.city_info(user_ip)['city_info']

    country_name = g.country_name(user_ip)['country_name']
    country_info = g.country_info(user_ip)['country_info']

    coords = g.coords(user_ip)['coords']


    context = {
        'user_ip': user_ip,
        'city_name': city_name,
        'country_name': country_name,
        'country_info': country_info,
        'city_info': city_info,
        'coords': coords
    }

    return render(request, 'base/surprise.html', context)
