from requests import get
from logging import warning

class ApisNetPe:

    BASE_URL = 'https://api.apis.net.pe'

    def _get(self, path: str, params: dict):

        url = f'{self.BASE_URL}{path}'

        headers = {
            'Authorization': 'apis-token-1.aTSI1U7KEuT-6bbbCguH-4Y8TI6KS73N', 
            'Referer': 'https://apis.net.pe/api-tipo-cambio.html'
        }

        print(url)

        response = get(url, headers=headers, params=params)

        print(response)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 422:
            warning(f'{response.url} - invalida parameter')
            warning(response.text)
        elif response.status_code == 403:
            warning(f'{response.url} - IP blocked')
        elif response.status_code == 429:
            warning(f'{response.url} - Many requests add delay')
        elif response.status_code == 401:
            warning(f'{response.url} - Invalid token or limited')
        else:
            warning(f'{response.url} - Server Error status_code={response.status_code}')
        return None

    def get_person(self, dni: str):      
        return self._get('/v1/dni', {'numero': dni})

    def get_company(self, ruc: str):
        return self._get('/v1/ruc', {'numero': ruc})

    def get_exchange_rate(self, date: str):
        return self._get('/v1/tipo-cambio-sunat', {'fecha': date})

    def get_exchange_rate_today(self):
        return self._get('/v1/tipo-cambio-sunat', {})

    def get_exchange_rate_for_month(self, month: int, year: int):
        return self._get('/v1/tipo-cambio-sunat', {'month': month, 'year': year})



# Buscamos el dni en la api de buscar dni
          #  APIS_TOKEN = 'apis-token-1.aTSI1U7KEuT-6bbbCguH-4Y8TI6KS73N'
          #  api_consultas = ApisNetPe(APIS_TOKEN)    
          #  dni = self.men1_agregar_buscar_dni.get()
          #  persona = api_consultas.get_person(dni)


#print(ApisNetPe().get_company('20511466629'))
print(ApisNetPe().get_person('48555618'))
#print(ApisNetPe().get_exchange_rate('2020-01-01'))
#print(ApisNetPe().get_exchange_rate_for_month(1, 2020))