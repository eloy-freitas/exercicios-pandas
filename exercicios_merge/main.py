import pandas as pd

if __name__ == '__main__':
    def read_xlsx(path):
        return pd.read_excel(path)

    # exercicio 1
    df_loja_a = read_xlsx('Datasets_merge/CadastroLoja_A.xlsx')
    print('\nexercicio 1:\n',df_loja_a.columns)
    df_loja_b = read_xlsx('Datasets_merge/CadastroLoja_B.xlsx')
    print(df_loja_b.columns)
    df_tipo_cliente = read_xlsx('Datasets_merge/TipoCliente.xlsx')
    print(df_tipo_cliente.columns)
    df_vendas = read_xlsx('Datasets_merge/Vendas.xlsx')
    print(df_vendas.columns)

    # exercicio 2
    print('\n\nexercicio 2:\ndf_loja_a head:\n',df_loja_a.head())
    print('\ndf_loja_a shape:\n',df_loja_a.shape)
    print('\ndf_loja_a dtypes:\n',df_loja_a.dtypes)

    print('\ndf_loja_b head:\n',df_loja_b.head())
    print('\ndf_loja_b shape:\n',df_loja_b.shape)
    print('\ndf_loja_b dtypes:\n',df_loja_b.dtypes)

    print('\ndf_tipo_cliente head:\n',df_tipo_cliente.head())
    print('\ndf_tipo_cliente shape:\n',df_tipo_cliente.shape)
    print('\ndf_tipo_cliente dtypes:\n',df_tipo_cliente.dtypes)

    print('\ndf_vendas head:\n',df_vendas.head())
    print('\ndf_vendas shape:\n',df_vendas.shape)
    print('\ndf_vendas dtypes:\n',df_vendas.dtypes)

    #exercicio 3
    print('\nexercicio 3:\n', 
        df_loja_a.set_index('ID').join(df_vendas.set_index('ID'), 
                                        how='inner'))
    
    #exercicio 4
    print('\nexercicio 4:\n',
        df_loja_b.set_index('ID').join(df_vendas.set_index('ID'), 
                                        how='inner'))

    #exercicio 5
    print('\nexercicio 5:\n',
        df_loja_a.set_index('ID').join(df_loja_b.set_index('ID'), 
                                        how='inner', 
                                        lsuffix='_cliente_a', 
                                        rsuffix='_cliente_b'))
    
    # exercicio 6
    print('\nexercicio 6:\n',
        df_loja_a.set_index('ID').join(df_loja_b.set_index('ID'), 
                                        how='inner', 
                                        lsuffix='_a', 
                                        rsuffix='_b'))

    # exercicio 7
    df_clientes = pd.concat([df_loja_a, df_loja_b], ignore_index=True)
    print('\nexercicio 7:\n', df_clientes)

    # exercicio 8
    print('\nexercicio 8:\n', df_clientes.drop_duplicates())
    

    # exercicio 9
    print('\nexercicio 9:\nTotal de gastos:', 
        df_loja_a.set_index('ID').join(df_vendas.set_index('ID'), 
                                        how='inner')['Valor'].sum())

    # exercicio 10    
    print(
        '\nexercicio 10:\n', 
                        pd.merge(
                                pd.merge(df_clientes, 
                                        df_vendas, 
                                        how='left'),
                                df_tipo_cliente, left_on='TipoCliente', 
                                right_on='ID'
                                )
                                .filter(
                                    items=['ID_x',
                                            'Nome',
                                            'Idade',
                                            'CEP',
                                            'TipoCliente_y',
                                            'Valor']))
    
    #exercicio 11
    print('\nexercicio 11:\n',
        df_loja_a.set_index('ID')
            .join(df_vendas.set_index('ID'))
            .query('Valor == "NaN"'))

    #exercicio 12
    print('\nexercicio 12:\n',
        df_loja_b.set_index('ID')
            .join(df_vendas.set_index('ID'))
            .query('Valor == "NaN"'))
    
    #exercicio 13
    print('\nexercicio 13:\n',
        df_clientes.set_index('ID')
            .join(df_vendas.set_index('ID'))
            .query('Valor == "NaN"')
            .drop_duplicates())

    #exercicio 14
    print('\nexercicio 14:\n',
        pd.merge(df_clientes, df_vendas, how='left')
            .query('Valor != "NaN"')
            .drop_duplicates())
    
    #exercicio 15
    print('\nexercicio 15:\n',
        pd.merge(df_clientes, df_vendas, how='left')
            .filter(items=['ID','Nome', 'Valor'])
            .groupby(by=['ID','Nome'])
            .sum()
            .sort_values(by='Valor',ascending=False)
            .head(3))
    
