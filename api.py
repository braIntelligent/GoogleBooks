import requests

class Api_books():
    def __init__(self, libro):
        self.__libro = libro

    def api(self):
        try:
            response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={self.__libro}")
            response.raise_for_status()
            if response.status_code == 200:
                data = response.json()
                return data
        except requests.ConnectionError as e:
            print(f"ERROR AL CONECTAR CON LA API: {e}")
        except requests.HTTPError as e:
            print(f"ERROR EN LA RESPUESTA DE LA API: {e}")
        except Exception as e:
            print(f"UN ERROR INESPERADO OCURRIÓ: {e}")
        return False
