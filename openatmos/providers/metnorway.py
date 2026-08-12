import requests

url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=-21.625&lon=-48.875"

headers = {
    "User-Agent": "https://github.com/MarceloDev-Py/OpenAtmos"
}

response = requests.get(url, headers=headers)

dados = response.json()

print(dados)