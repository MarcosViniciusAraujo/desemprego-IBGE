import requests
import matplotlib.pyplot as plt
import pandas as pd

API = 'https://apisidra.ibge.gov.br/values/t/6381/n1/all/v/4099/p/all/d/v4099%201'


def main():

    # Chamando a API
    req = requests.get(API)
    raw = req.json()

    # Separação de colunas
    nivelDesemprego = [float(tri['V']) for tri in raw[1:]]
    trimestrMovel = [tri['D3N'] for tri in raw[1:]]

    # Criação do Dataframe
    dfDesempregoTri = pd.DataFrame(
            nivelDesemprego, 
            index=trimestrMovel, 
            columns=['Desemprego']
        )

    # Exibição do gráfico
    dfDesempregoTri.plot.line()
    plt.xticks(rotation='vertical')
    plt.ylabel('Taxa de desemprego - (%)')
    plt.title('Taxa de Desemprego (2012 - Hoje)')
    plt.show()


if __name__ == '__main__':
    main()