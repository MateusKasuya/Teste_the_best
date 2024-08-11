import pandas as pd

def transform_dataframe(df : pd.DataFrame) -> pd.DataFrame:
    """
    Essa função recebe um dataframe extraído de uma base csv e realiza as tratativas adequadas para o carregamento do arquivo
    """

    for column in df.columns:
        if column in ['data_cadastro', 'data_pedido']:
            # Transforma a coluna no tipo datetime
            df[column] = pd.to_datetime(df[column])
        
        elif column in ['preco', 'valor_total', 'quantidade', 'preco_unitario']:
            # Corrige valores negativos para o seu equivalente positivo
            df[column] = df[column].abs()

    return df
