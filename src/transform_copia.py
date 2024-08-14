# Mesmo arquivo do transform.py, é utilizado no pytest test_transform.py

import pandas as pd
import pandera as pa

from schema import (
    ClientesSchema,
    ItensPedidosSchema,
    PedidosSchema,
    ProdutosSchema,
)


@pa.check_output(ClientesSchema, lazy=True)
def transform_clientes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Essa função recebe um dataframe e realiza as tratativas adequadas:
    Garante que as colunas de data sejam transformadas no time correto.
    Transforma as colunas númericas de quantidade e valores sempre em números positivos
    """

    try:
        for column in df.columns:
            if column in ['data_cadastro', 'data_pedido']:
                # Transforma a coluna no tipo datetime
                df[column] = pd.to_datetime(df[column])

            elif column in [
                'preco',
                'valor_total',
                'quantidade',
                'preco_unitario',
            ]:
                # Corrige valores negativos para o seu equivalente positivo
                df[column] = df[column].abs()
        print('DataFrame transformado com sucesso.')
        return df

    except Exception as e:
        print(f'Erro ao carregar o arquivo {df}: {e}')
        return None


@pa.check_output(ItensPedidosSchema, lazy=True)
def transform_itenspedidos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Essa função recebe um dataframe e realiza as tratativas adequadas:
    Garante que as colunas de data sejam transformadas no time correto.
    Transforma as colunas númericas de quantidade e valores sempre em números positivos
    """

    try:
        for column in df.columns:
            if column in ['data_cadastro', 'data_pedido']:
                # Transforma a coluna no tipo datetime
                df[column] = pd.to_datetime(df[column])

            elif column in [
                'preco',
                'valor_total',
                'quantidade',
                'preco_unitario',
            ]:
                # Corrige valores negativos para o seu equivalente positivo
                df[column] = df[column].abs()
        print('DataFrame transformado com sucesso.')
        return df

    except Exception as e:
        print(f'Erro ao carregar o arquivo {df}: {e}')
        return None


@pa.check_output(PedidosSchema, lazy=True)
def transform_pedidos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Essa função recebe um dataframe e realiza as tratativas adequadas:
    Garante que as colunas de data sejam transformadas no time correto.
    Transforma as colunas númericas de quantidade e valores sempre em números positivos
    """

    try:
        for column in df.columns:
            if column in ['data_cadastro', 'data_pedido']:
                # Transforma a coluna no tipo datetime
                df[column] = pd.to_datetime(df[column])

            elif column in [
                'preco',
                'valor_total',
                'quantidade',
                'preco_unitario',
            ]:
                # Corrige valores negativos para o seu equivalente positivo
                df[column] = df[column].abs()
        print('DataFrame transformado com sucesso.')
        return df

    except Exception as e:
        print(f'Erro ao carregar o arquivo {df}: {e}')
        return None


@pa.check_output(ProdutosSchema, lazy=True)
def transform_produtos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Essa função recebe um dataframe e realiza as tratativas adequadas:
    Garante que as colunas de data sejam transformadas no time correto.
    Transforma as colunas númericas de quantidade e valores sempre em números positivos
    """

    try:
        for column in df.columns:
            if column in ['data_cadastro', 'data_pedido']:
                # Transforma a coluna no tipo datetime
                df[column] = pd.to_datetime(df[column])

            elif column in [
                'preco',
                'valor_total',
                'quantidade',
                'preco_unitario',
            ]:
                # Corrige valores negativos para o seu equivalente positivo
                df[column] = df[column].abs()
        print('DataFrame transformado com sucesso.')
        return df

    except Exception as e:
        print(f'Erro ao carregar o arquivo {df}: {e}')
        return None
