import pandas as pd
from extract import extract_csv_to_dataframe
from transform import transform_dataframe

def run_etl():

    # File Paths dos CVS
    clientes_csv = 'data/clientes 2(in).csv'
    itenspedido_csv = 'data/itens_pedido 2(in).csv'
    pedidos_csv = 'data/pedidos 2(in).csv'
    produtos_csv = 'data/produtos 2(in).csv'

    # Realizar Extração dos arquivos
    clientes_df = extract_csv_to_dataframe(clientes_csv)
    itenspedido_df = extract_csv_to_dataframe(itenspedido_csv)
    pedidos_df = extract_csv_to_dataframe(pedidos_csv)
    produtos_df = extract_csv_to_dataframe(produtos_csv)

    # Aplicar Transformação no dataframe
    clientes_df_transformed = transform_dataframe(clientes_df)
    itenspedido_df_transformed = transform_dataframe(itenspedido_df)
    pedidos_df_transformed = transform_dataframe(pedidos_df)
    produtos_df_transformed = transform_dataframe(produtos_df)

    return None

if __name__ == '__main__':
    run_etl()