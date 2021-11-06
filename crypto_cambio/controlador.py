from crypto_cambio.modelo import CryptoModelo
from crypto_cambio.vista import CryptoVista




class CryptoControlador:
    def __init__(self):
        self.vista = CryptoVista()
        self.modelo = CryptoModelo()


    def ejecutar(self):
        salir = "n"
        while salir != "n":
            desde, hasta = self.vista.pedir_info_monedas()
            self.modelo.moneda_origen = desde
            self.modelo.moneda_destino = hasta
            self.modelo.exchange()
            self.vista.mostrar(desde, hasta, self.modelo.cambio)

        salir = input("¿Quieres seguir cambiando? s/n ").lower()
        