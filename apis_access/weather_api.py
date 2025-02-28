import requests


def get_weather(
    city,
    units='metric',
):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid=26631f0f41b95fb9f5ac0df9a8f43c92&units={units}"
    r = requests.get(url)
    content = r.json()
    with open('data.txt', 'a') as file:
        for dicty in content['list']:
            file.write(
                f"{dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n"
            )
    return content


print(get_weather(city='Washington'))
