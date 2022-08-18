#%%
# imports
import requests
import json

#%%
url = 'http://economia.awesomeapi.com.br/last/USD-BRL'
ret = requests.get(url)

# %%
dolar = json.loads(ret.text)['USDBRL']
dolar['code']
# %%
print(f"20 dólares custam {float(dolar['bid']) * 20} reais")

# %%
def cotacao(valor, moeda):
    url = f"http://economia.awesomeapi.com.br/last/{moeda}"
    ret = requests.get(url)
    cot = json.loads(ret.text)[moeda.replace('-','')]

    # printando a mensagem
    print(f"{valor} {cot['code']} hoje custam {float(cot['bid']) * valor} {cot['codein']}")


# %%
cotacao(20, 'USD-BRL')
# %%
cotacao(20, 'JPY-BRL')
# %%
# Tratando erros genéricos
try:
    cotacao(20, 'joao')
except:
    pass


# %%
import backoff
# %%
