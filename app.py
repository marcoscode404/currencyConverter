import requests

def conversor_moedas(valor, de_moeda, para_moeda):
    url = f"https://api.exchangerate-api.com/v4/latest/{de_moeda}"
    response = requests.get(url)
    dados = response.json()
    taxa = dados['rates'][para_moeda]
    return valor * taxa

valor = 100  # valor em USD
print(f"{valor} BRL é igual a {conversor_moedas(valor, 'BRL', 'USD')} USD")
