import requests
apikey ="E73C6DE3-AE29-4E9C-B6E2-E4B0F8B037F9"

cripto = input("introduzca una croipto conocida: ")
while cripto != "":

    r = requests.get("https://rest.coinapi.io/v1/exchangerate/{}/EUR?apikey={}".format(cripto, apikey))

    resultado = r.json()
    if r.status_code == 200:
        print("{:.2f} €".format(resultado["rate"]))
    else:
        print(resultado["error"])
    
    cripto = input("Introduzca una cripto conocida: ")


