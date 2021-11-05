import requests


pregunta = "Y"
while pregunta.upper() == "Y":
    moneda_origen = input("¿Que moneda quieres cambiar?")
    moneda_destino = input("¿Que moneda quieres obtener?")

    url = f"https://rest.coinapi.io/v1/exchangerate/{moneda_origen}/{moneda_destino}"
    cambio = requests.get(url, headers=headers)
    exchange = cambio.json()["rate"]
    print("1 {}, es igual a {:,.2f} {}".format(moneda_origen, exchange, moneda_destino))
    pregunta = input("Quieres cambiar algo mas? (S/N)")