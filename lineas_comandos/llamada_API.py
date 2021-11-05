import requests

apiKey = '80CDBBD8-8C86-42DA-BA3F-499D14C79045'
headers = {
    "X-CoinAPI-Key": apiKey
}

url = f"https://rest.coinapi.io/v1/exchanges"

respuesta = requests.get(url, headers=headers)
codigo = respuesta.status_code

if codigo == 200:
    print(respuesta.text)
else:
    print(codigo, respuesta.reason)
    print(respuesta.json())


