from django.shortcuts import render
import json 
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=02fe2c28c75be844ab881298a5b30370').read()
        json_data = json.loads(res.decode('utf-8'))
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon'])+' '+  # fix typo ('Ion' to 'lon')
            str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+"k",
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        data = {}
        city = ''
    return render(request, 'index.html', {'city':city, 'data':data})
