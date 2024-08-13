import pandera as pa
from pandera.typing import Series
import pandas as pd

class ProdutosSchema(pa.DataFrameModel):

    produto_id : Series[int] = pa.Field(gt = 0)
    nome : Series[str]
    categoria : Series[int] = pa.Field(gt = 0)
    preco : Series[float] = pa.Field(gt = 0)

    class Config:
        coerce = True
        strict = True

@pa.check_output(ProdutosSchema, lazy=True)
def transform_dataframe(df : pd.DataFrame) -> pd.DataFrame:
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
            
            elif column in ['preco', 'valor_total', 'quantidade', 'preco_unitario']:
                # Corrige valores negativos para o seu equivalente positivo
                df[column] = df[column].abs()
        print('DataFrame transformado com sucesso.')
        return df
    
    except Exception as e:
        print(f"Erro ao carregar o arquivo {df}: {e}")
        return None
    
df = pd.DataFrame({
    'produto_id': [1, 2, 3],
    'nome': ['Produto A', 'Produto B', 'Produto C'],
    'categoria': ['a', 'b', 'c'],
    'preco': [10.0, -5.0, 20.0],
})

transformed_df = transform_dataframe(df)
print(transformed_df)