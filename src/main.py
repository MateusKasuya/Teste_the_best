import pandas as pd
import pandera as pa

from database import Base, SessionLocal, engine
from extract import extract_csv_to_dataframe
from load import load_dataframe_to_postgres
from models import ClienteBase, ItensPedidosBase, PedidosBase, ProdutosBase
from transform import (
    transform_clientes,
    transform_itenspedidos,
    transform_pedidos,
    transform_produtos,
)


def run_etl():

    Base.metadata.create_all(engine)

    session = SessionLocal()

    # File Paths dos CVS
    clientes_csv = 'data/clientes 2(in).csv'
    produtos_csv = 'data/produtos 2(in).csv'
    pedidos_csv = 'data/pedidos 2(in).csv'
    itenspedido_csv = 'data/itens_pedido 2(in).csv'

    # Realizar Extração dos arquivos
    clientes_df = extract_csv_to_dataframe(clientes_csv)
    produtos_df = extract_csv_to_dataframe(produtos_csv)
    pedidos_df = extract_csv_to_dataframe(pedidos_csv)
    itenspedido_df = extract_csv_to_dataframe(itenspedido_csv)

    # Aplicar Transformação no dataframe
    clientes_df_transformed = transform_clientes(clientes_df)
    produtos_df_transformed = transform_produtos(produtos_df)
    pedidos_df_transformed = transform_pedidos(pedidos_df)
    itenspedido_df_transformed = transform_itenspedidos(itenspedido_df)

    # Carrega a tabela no banco de dados
    load_dataframe_to_postgres(clientes_df_transformed, ClienteBase, session)
    load_dataframe_to_postgres(produtos_df_transformed, ProdutosBase, session)
    load_dataframe_to_postgres(pedidos_df_transformed, PedidosBase, session)
    load_dataframe_to_postgres(
        itenspedido_df_transformed, ItensPedidosBase, session
    )


if __name__ == '__main__':
    run_etl()
