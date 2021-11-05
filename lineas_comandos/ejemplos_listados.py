import requests

apiKey = '80CDBBD8-8C86-42DA-BA3F-499D14C79045'
headers = {
    "X-CoinAPI-Key": apiKey
}
url = f"https://rest.coinapi.io/v1/assets"

respuesta = requests.get(url, headers=headers)
resultado = respuesta.json()

for i in range(12):
    moneda = resultado[i]
    print(moneda["asset_id"],"|", moneda["name"], "|", moneda["data_end"])
    
    print("-"*20)
-----------------------------------------------------------------------------------

    # PARA QUE DEVULEVA TODAS LAS MONEDAS


respuesta = requests.get(url, headers=headers)
resultado = respuesta.json()

for moneda in resultado:
    #moneda = resultado[i]
    print(moneda["asset_id"],"|", moneda["name"], "|", moneda["data_end"])
    
    print("-"*20)
-----------------------------------------------------------------------------------
    # PARA QUE DEVUELVA RESULTADOS PORLA PRIMERA LETRA QUE ELIJAS


    respuesta = requests.get(url, headers=headers)
    resultado = respuesta.json()

for moneda in resultado:
    if moneda["asset_id"][0] == "E":
        print(moneda["asset_id"],"|", moneda["name"], "|", moneda["data_end"])
    
        print("-"*20)
----------------------------------------------------------------------------------
    #PARA LLAMAR SOLO A LAS QUE EMPIEZEN POR EUR POR EJEMPLO

    respuesta = requests.get(url, headers=headers)
    resultado = respuesta.json()

for moneda in resultado:
    if moneda["asset_id"].startswith("EUR"):
        print(moneda["asset_id"],"|", moneda["name"], "|", moneda["data_end"])
    
        print("-"*20)
-----------------------------------------------------------------------------------
