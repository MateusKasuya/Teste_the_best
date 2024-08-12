import pandas as pd

def transform_dataframe(df : pd.DataFrame) -> pd.DataFrame:
    """
    Essa função recebe um dataframe e realiza as tratativas adequadas
    """

    try:
        for column in df.columns:
            if column in ['data_cadastro', 'data_pedido']:
                # Transforma a coluna no tipo datetime
                df[column] = pd.to_datetime(df[column])
            
            elif column in ['preco', 'valor_total', 'quantidade', 'preco_unitario']:
                # Corrige valores negativos para o seu equivalente positivo
                df[column] = df[column].abs()
        print('DataFrame transformado com sucesso.')
        return df
    
    except Exception as e:
        print(f"Erro ao carregar o arquivo {df}: {e}")
        return None

