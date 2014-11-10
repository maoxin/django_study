from django.shortcuts import render, get_object_or_404
# from django.contrib.gis.utils import GeoIP
# with libgeoip-dev and GeoIP
import requests
from star.models import Star
from ipware.ip import get_ip

def index(request):
    ip = get_ip(request)
    # geo = GeoIP()
    ip2location = requests.get('http://ipinfo.io/%s/json/' %ip).json()
    print ip2location
    latitude, longitude = eval(ip2location['loc'])
    context = {
        'star_color': get_object_or_404(Star, star_name='earth').star_color,
        'ip': ip,
        'latitude': latitude,
        'longitude': longitude,
    }
    
    
    return render(request, 'star/index.html', context)
