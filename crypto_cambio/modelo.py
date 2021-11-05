import requests
from crypto_cambio import apiKey

from crypto_cambio import URL_SIN_PARAMETROS



class ErrorAPI(Exception):
    pass
    


class CryptoModelo():
    def __init__(self):
        self.moneda_origen = ""
        self.moneda_destino = ""
        self.cambio = 0.0
            pass

    def exchange(self):
        cabecera = {
            "X-CoinAPI-Key": apiKey
        }
        url = f"https://rest.coinapi.io/v1/exchangerate/{self.moneda_origen}/{self.moneda_destino}"
        #url = URL_SIN_PARAMETROS.format(orig=self.moneda_origen, dest=self.moneda_destino)
        result = requests.get(url, headers=cabecera)

        if result.status_code == 200:
             self.cambio = result.json()["rate"]
        else:
            raise ErrorAPI(
                "Ha ocurrido un error {} al consultar la API".format(result.status_code)
         )

  