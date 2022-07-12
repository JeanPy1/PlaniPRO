from requests import get
from logging import warning

def __conexion(params: dict):

    url = 'https://api.apis.net.pe/v1/dni'

    headers = {'Authorization': 'apis-token-1.aTSI1U7KEuT-6bbbCguH-4Y8TI6KS73N', 
               'Referer'      : 'https://apis.net.pe/api-tipo-cambio.html'}        

    response = get(url, headers=headers, params=params)
        
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

def search(dni: str):

    return __conexion({'numero': dni})