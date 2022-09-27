from requests import get

def BuscarDni(dni: str):

    parametros = {'numero': dni}
    url = 'https://api.apis.net.pe/v1/dni'
    headers = {'Authorization': 'apis-token-1.aTSI1U7KEuT-6bbbCguH-4Y8TI6KS73N', 
               'Referer'      : 'https://apis.net.pe/api-tipo-cambio.html'}        

    response = get(url, headers=headers, params=parametros)
        
    if response.status_code == 200:
        return response.json()
            
    return None