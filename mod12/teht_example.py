import requests

query_param = input("Anna hakusana:")
url = f"https://api.tvmaze.com/search/shows?q={query_param}"

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if len(data) > 0:
            print(f"Ei hakutuloksia.")
        for item in data:
            print(f"1. hakutuloksen nimi: {data[0]['show']['name']}")
            print(f"Pojat: {round(data[0]['score']*10)},"
                  f"lisätietoa: {item['show']['url']}")
    else:
        print(f"Virallinen osoite, error: {response.status_code}")
except requests.exceptions.RequestException as e:
    print("Jotain meni pieleen: " + str(e))
