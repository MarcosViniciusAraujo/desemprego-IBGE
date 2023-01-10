# **Taxa de desemprego (2012 - Hoje)**

## **Instalação**

Antes de executar o programa, é necessário instalar as seguintes biliotecas:

-   Python 3.4+
-   Requests
-   Matplotlib
-   Pandas

Caso não possua alguma dessas bibliotecas, basta executar os seguintes comandos no terminal:

-   Caso não possua **Requests**:

```bash
pip install requests
```

-   Caso não possua **Matplotlib**:

```bash
pip install matplotlib
```

-   Caso não possua **Pandas**:

```bash
pip install pandas
```

## **Execução**

Após instaladas as dependências, o programa deve ser executado da seguinte forma:

```powershell
python desemprego.py
```

O reposítório também contém o arquivo `desemprego.ipynb`, sendo um **Jupyter Notebook** com todo o desenvolvimento do proejto

## **Resultados**

Após executado, o programa exibirá um gráfico similiar ao seguinte:

![](/img/line-chart-desemprego.png)

## **Fonte**

Para construção desse programa, foi necessário o uso de uma **API**, que foi retirada do site oficial do [**IBGE**](https://sidra.ibge.gov.br/pesquisa/pnadcm/tabelas).
