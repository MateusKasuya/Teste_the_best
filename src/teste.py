# main.py

import pandera as pa

from src.database import Base, SessionLocal, engine
from src.extract import extract_csv_to_dataframe
from src.load import load_data_to_db
from src.models import ClienteBase, ItensPedidosBase, PedidosBase, ProdutosBase
from src.schema import (
    ClientesSchema,
    ItensPedidosSchema,
    PedidosSchema,
    ProdutosSchema,
)
from src.transform import transform_dataframe


def validate_data(df, schema):
    """
    Valida um DataFrame utilizando o schema fornecido.

    df -> DataFrame que será validado.
    schema -> Classe SchemaModel do Pandera correspondente ao DataFrame.
    """
    try:
        validated_df = schema.validate(df)
        print(
            f'Validação do DataFrame {schema.__name__} concluída com sucesso.'
        )
        return validated_df
    except pa.errors.SchemaError as e:
        print(f'Erro de validação no DataFrame {schema.__name__}: {e}')
        return None


def run_etl():
    # Cria as tabelas no banco de dados
    Base.metadata.create_all(engine)

    # Cria uma sessão do banco de dados
    session = SessionLocal()

    # Extração e Transformação
    clientes_df = extract_csv_to_dataframe('clientes.csv')
    produtos_df = extract_csv_to_dataframe('produtos.csv')
    pedidos_df = extract_csv_to_dataframe('pedidos.csv')
    itens_pedidos_df = extract_csv_to_dataframe('itens_pedidos.csv')

    if clientes_df is not None:
        clientes_df = transform_dataframe(clientes_df)
        clientes_df = validate_data(clientes_df, ClientesSchema)
        if clientes_df is not None:
            load_data_to_db(clientes_df, ClienteBase, session)

    if produtos_df is not None:
        produtos_df = transform_dataframe(produtos_df)
        produtos_df = validate_data(produtos_df, ProdutosSchema)
        if produtos_df is not None:
            load_data_to_db(produtos_df, ProdutosBase, session)

    if pedidos_df is not None:
        pedidos_df = transform_dataframe(pedidos_df)
        pedidos_df = validate_data(pedidos_df, PedidosSchema)
        if pedidos_df is not None:
            load_data_to_db(pedidos_df, PedidosBase, session)

    if itens_pedidos_df is not None:
        itens_pedidos_df = transform_dataframe(itens_pedidos_df)
        itens_pedidos_df = validate_data(itens_pedidos_df, ItensPedidosSchema)
        if itens_pedidos_df is not None:
            load_data_to_db(itens_pedidos_df, ItensPedidosBase, session)


if __name__ == '__main__':
    run_etl()
