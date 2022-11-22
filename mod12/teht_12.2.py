import requests

base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "e637ea82f6ff2a50f09cf283c917dd77"
city = input("Syötä kaupunki: ")
url = f"{base_url}appid={api_key}&q={city}&units=metric&lang=fi"
# testaa ensin, että osoite on oikein muodostettu
# print(url)
try:
    response = requests.get(url)
    if response.status_code == 200:
        json_response = response.json()
        temp = json_response['main']['temp']
        description = json_response['weather'][0]['description']
        country = json_response['sys']['country']
        print(f"{country}\n"
              f"{city}\n"
              f"Lämpötila: {temp}°C\n"
              f"Sää: {description}")
    elif response.status_code == 404:
        print(f"Kaupunkia: {city}, ei löydy :(")
    else:
        print(f"Verkko toimi ja palvelin vastasi, mutta joku muu virhe: {response.status_code}")

except requests.exceptions.RequestException as e:
    print("hakua ei voitu suorittaa" + str(e))