from django.shortcuts import render
import requests
# Create your views here.

my_url = "https://api.openweathermap.org/data/2.5/weather"
apikey = "2cd5682b8204d1e16c250776bda23fad"

def weather(request):
    city = request.GET.get('city')
    if city:
        url = f'{my_url}?q={city}&appid={apikey}'
        response = requests.get(url)
        data = response.json()
        weather_data = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return render(request, 'weather.html', {'weather_data': weather_data})
    else:
        return render(request, 'weather.html')