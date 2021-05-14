# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime

import pandas as pd
pd.options.display.float_format = '{:.2f}'.format

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filename = 'imoveis.csv'

    #exercicio 1
    df = pd.read_csv(filename)

    #exercicio 2
    print("\nexercicio 2\n",df.shape)

    #exercicio 3
    print("\nexercicio 3\n",df.head(10))

    #exercicio 4
    print("\nexercicio 4\n",df.columns)

    #exercicio 5
    print("\nexercicio 5\n",df.dtypes)

    #exercicio 6
    def corrigirdata(data):
        ano = int(data[:4])
        mes = int(data[4: 6])
        dia = int(data[6: 8])
        return datetime.datetime(ano, mes, dia)

    df['data'] = list(map(corrigirdata, df['data']))
    print("\nexercicio 6:\n",df['data'].dtypes)

    #exercicio 7
    df["analise"] = 2021
    print("\nexercicio 7\n",df['analise'])

    #apenas corrigindo o nome das colunas
    df.rename(columns={'preÃ§o': 'preco',
                       'condiÃ§Ã£o': 'condicao',
                       'metragem do porÃ£o': 'metragem do portao',
                       'ano de construÃ§Ã£o': 'ano de construcao',
                       'ano de renovaÃ§Ã£o': 'ano de renovacao',
                       'cÃ³digo postal': 'codigo postal',
                       'Ã¡rea Ãºtil em 2015': 'area util em 2015',
                       'Ã¡rea do lote em 2015': 'area do lote em 2015'}, inplace= True)

    #exercicio 8
    print("\nexercicio 8: \n",df[['id', 'data', 'preco', 'banheiros', 'ano de construcao']])

    #exercicio 9
    df.pop('metragem da casa.1')

    #exercicio 10
    def corrigirvalor(valor):
        return int(float(valor.replace(',', '.')))

    df['banheiros'] = list(map(corrigirvalor, df['banheiros']))
    print("\nexercicio 10\n", df['banheiros'])
    
    #exercicio 11
    print("\nexercicio 11: \n", df[df['ano de construcao'] < 2000])

    #exercicio 12
    df.rename(columns={'data': 'DT_REFERENCIA',
                       'preco': 'VL_PRECO',
                       'quartos': 'QTD_QUARTOS',
                       'banheiros': 'QTD_BANHEIROS',
                       'ano de construcao': 'DT_ANO_CONSTRUCAO',
                       'codigo postal': 'NU_CEP',
                       'latitude': 'NU_LATITUDE',
                       'longitude': 'NU_LONGITUDE',
                       'andares': 'QTD_ANDARES',
                       'orla': 'FL_ORLA',
                       'vista': 'FL_VISTA'}, inplace=True)

    print("\nexercicio 12\n",df.columns)

    #exercicio 13
    def criarcoluna(condicao):
        if condicao < 2:
            return 'ruim'
        elif condicao >= 3 and condicao <=4:
            return 'regular'
        else:
            return 'bom'

    df['DS_TIPO_CONDICAO'] = list(map(criarcoluna, df['condicao']))

    print("\nexercicio 13:\n", df['DS_TIPO_CONDICAO'])

    #exercicio 14
    def corrigirpreco(valor):
        if not valor.isalnum():
            numero = valor.replace(',', '.')
            numero = numero.split('E+')
            return float(numero[0]) * 10 ** int(numero[1])
        else:
            return float(valor)

    df['VL_PRECO'] = list(map(corrigirpreco, df['VL_PRECO']))
    print("\nexercicio 14: \n",df[['id', 'VL_PRECO']].sort_values(by='VL_PRECO',ascending=False))

    #exercicio 15
    print("\nexercicio 15: \nquantidade:",
          df[df['DS_TIPO_CONDICAO'] == 'regular'].shape[0])

    #exercicio 16
    print("\nexercicio 16:\npreço médio: {:.2f}".
          format(float(df[df['DS_TIPO_CONDICAO'] == 'regular'].filter(items=['VL_PRECO']).mean())))

    #exercicio 17
    print("\nexercicio 17:\npreço: {:.2f}".
          format(float(df[df['QTD_QUARTOS'] == 3].filter(items=['VL_PRECO']).max())))

    #exercicio 18
    print("\nexercicio 18: \nquantidade: ",
          df[(df['DS_TIPO_CONDICAO'] == 'bom') & (df['QTD_QUARTOS'] > 2) & (df['QTD_BANHEIROS'] > 2)].shape[0])

    #exercicio 19
    print("\nexercicio 19: \nid do preço max: ",
          int(df[['id', 'VL_PRECO']].max().filter(items=['id'])))

    print("\nexercicio 19: \nid do preço min: ",
          int(df[['id', 'VL_PRECO']].min().filter(items=['id'])))

    #exercicio 20
    print("\nexercicio 20: \n",
          df[['DT_ANO_CONSTRUCAO']].min())

    #exercicio 21
    print("\nexercicio 21: \n",
          df[['id', 'DS_TIPO_CONDICAO']].groupby(by=['DS_TIPO_CONDICAO']).count())

    #exercicio 22
    print("\nexercicio 22: \n",
         df[['id', 'DT_ANO_CONSTRUCAO']].groupby(by=['DT_ANO_CONSTRUCAO']).mean())

    #exercicio 23
    print("\nexercicio 23: \n",
          df[['DT_ANO_CONSTRUCAO', 'QTD_QUARTOS']].groupby(by='DT_ANO_CONSTRUCAO').count().min())

    #exercicio 24
    print("\nexercicio 24: \n",
          df[['QTD_QUARTOS', 'QTD_BANHEIROS','VL_PRECO']].groupby(by=['QTD_QUARTOS', 'QTD_BANHEIROS']).sum())

    #exercicio 25
    print("\nexercicio 25: \n",
          df[['DT_ANO_CONSTRUCAO', 'VL_PRECO']].groupby(by=['DT_ANO_CONSTRUCAO']).median())

    #exercicio 26
    classificacao = []
    for preco in df['VL_PRECO']:
        if preco < 321950:
            classificacao.append(0)
        elif preco >= 321950 and preco <= 450000:
            classificacao.append(1)
        elif preco > 450000 and preco <= 645000:
            classificacao.append(2)
        else:
            classificacao.append(3)

    df['CD_CLASSIFICACAO'] = classificacao

    print("\nexercicio 26: \n",
          df[['VL_PRECO','CD_CLASSIFICACAO']])

    #exercicio 27
    df['CD_CLASSIFICACAO'] = list(map(lambda x: 0 if x < 321950 else
        1 if x >= 321950 and x <= 450000 else
        2 if x> 450000 and x <= 645000 else 3, df['VL_PRECO']))
    print("\nexercicio 27: \n",
        df[['VL_PRECO', 'CD_CLASSIFICACAO']])

    #exercicio 28
    print("\nexercicio 28: \n",
        df[['NU_CEP', 'VL_PRECO']].groupby(by=['NU_CEP']).mean())
    df[['NU_CEP', 'VL_PRECO']].groupby(by=['NU_CEP']).mean().to_csv('saida.csv', index=True)






