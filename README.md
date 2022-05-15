# Ant Colony Clustering Algorithm

Implementação do algoritmo Ant Colony Clustering em Python.

## Execução

Execute o comando `py src/main.py` ou `python src/main.py` no seu terminal de preferência. Os resultados do algoritmo serão exibidos no próprio terminal.

## Configurações

O algoritmo pode ser configurado modificando as seguintes constantes no arquivo `src/consts.py`:

|Constante      |Significado                                        |
|:--------------|:--------------------------------------------------|
|S              |Tamanho da vizinhança (neighborhood)               |
|KP             |Probabilidade de pegar (pick)                      |
|KD             |Probabilidade de deixar (drop)                     |
|ALPHA          |Dependência entre os dados                         |
|ANT_QUANTITY   |Quantidade de formigas na colônia                  |
|MAX_ITERATIONS |Quant. máxima de iterações na fase de agrupamento  |
|ITEMS_DATA     |Dados que serão agrupados                          |
