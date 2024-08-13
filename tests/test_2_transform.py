import pandas as pd
import pandera as pa
import pytest

from src.transform_copia import (
    transform_clientes,
    transform_itenspedidos,
    transform_pedidos,
    transform_produtos,
)


# Exemplo de dados para testes
def create_test_dataframe(schema):
    if schema == 'clientes':
        return pd.DataFrame(
            {
                'cliente_id': [1, 2],
                'nome': ['mateus', 'victor'],
                'email': ['mateus@hotmail.com', 'kasuya@gmail.com'],
                'data_cadastro': ['2023-07-01', '2023-08-15'],
            }
        )
    elif schema == 'itenspedidos':
        return pd.DataFrame(
            {
                'item_pedido_id': [3, 4],
                'pedido_id': [5, 6],
                'produto_id': [7, 8],
                'quantidade': [-5, 10],
                'preco_unitario': [50, 70],
            }
        )
    elif schema == 'pedidos':
        return pd.DataFrame(
            {
                'pedido_id': [9, 10],
                'cliente_id': [11, 12],
                'data_pedido': ['2023-05-01', '2023-06-20'],
                'valor_total': [-300.0, 400.0],
            }
        )
    elif schema == 'produtos':
        return pd.DataFrame(
            {
                'produto_id': [13, 14],
                'nome': ['colher', 'vassoura'],
                'categoria': ['cozinha', 'casa'],
                'preco': [-150.0, 250.0],
            }
        )
    return pd.DataFrame()


# Testa a transformação de clientes
def test_transform_clientes():
    df = create_test_dataframe('clientes')
    transformed_df = transform_clientes(df)

    assert transformed_df is not None
    assert pd.api.types.is_datetime64_any_dtype(
        transformed_df['data_cadastro']
    )


# Testa a transformação de itens pedidos
def test_transform_itenspedidos():
    df = create_test_dataframe('itenspedidos')
    transformed_df = transform_itenspedidos(df)

    assert transformed_df is not None
    assert (transformed_df['quantidade'] >= 0).all()
    assert (transformed_df['preco_unitario'] >= 0).all()


# Testa a transformação de pedidos
def test_transform_pedidos():
    df = create_test_dataframe('pedidos')
    transformed_df = transform_pedidos(df)

    assert transformed_df is not None
    assert pd.api.types.is_datetime64_any_dtype(transformed_df['data_pedido'])
    assert (transformed_df['valor_total'] >= 0).all()


# Testa a transformação de produtos
def test_transform_produtos():
    df = create_test_dataframe('produtos')
    transformed_df = transform_produtos(df)

    assert transformed_df is not None
    assert (transformed_df['preco'] >= 0).all()
