import requests

def get_weather():
    api_key = "fe0293921024d520fd3d8567f3b82633"
    city = "Orlando"
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid= " + api_key + "&units=imperial"
    #https://api.openweathermap.org/data/2.5/weather?q=London&appid={API key}

    request = requests.get(url)
    json = request.json()
    print(json)

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {'description': description,
            'temp_min': temp_min,
            'temp_max': temp_max}


def main():
    weather_dict = get_weather()
    #print the results
    print("Today's forcase is", weather_dict.get('description'))
    print("The minimum temperate is", weather_dict.get('temp_min'))
    print("The maximum temperate is", weather_dict.get('temp_max'))

main()