import pandera as pa
from pandera.typing import Series
import pandas as pd

email_regex = r"[^@]+@[^@]+\.[^@]+"

class ClientesSchema(pa.DataFrameModel):
    """
    Classe para o schema Cliente que herda a validação do pandera Schema Model

    cliente_id: Inteiros Positivos
    nome: String
    email: validado pela variável regex email_regex
    data_cadastro: DateTime

    Config:
    coerce: converte os dados para os tipos definidos
    strict: exige que o dataframe tenha as mesmas colunas do schema
    """
    cliente_id : Series[int] = pa.Field(gt = 0)
    nome : Series[str]
    email : Series[str] = pa.Field(regex = email_regex)
    data_cadastro  : Series[pd.Timestamp] = pa.Field()

    class Config:
        coerce = True
        strict = True

class ProdutosSchema(pa.DataFrameModel):
    """
    Classe para o schema Produtos que herda a validação do pandera Schema Model

    produto_id: Inteiros Positivos
    nome: String
    categoria: String
    preco: Float Não Negativo

    Config:
    coerce: converte os dados para os tipos definidos
    strict: exige que o dataframe tenha as mesmas colunas do schema
    """
    produto_id : Series[int] = pa.Field(gt = 0)
    nome : Series[str]
    categoria : Series[str]
    preco : Series[float] = pa.Field(ge = 0)

    class Config:
        coerce = True
        strict = True

class PedidosSchema(pa.DataFrameModel):
    """
    Classe para o schema Pedidos que herda a validação do pandera Schema Model

    pedido_id: Inteiros Positivos
    cliente_id: Inteiros Positivos
    data_pedido: DateTime
    valor_total: Float Não Negativo

    Config:
    coerce: converte os dados para os tipos definidos
    strict: exige que o dataframe tenha as mesmas colunas do schema
    """
    pedido_id : Series[int] = pa.Field(gt = 0)
    cliente_id : Series[int] = pa.Field(gt = 0)
    data_pedido : Series[pd.Timestamp] = pa.Field()
    valor_total : Series[float] = pa.Field(ge = 0)

    class Config:
        coerce = True
        strict = True

class ItensPedidosSchema(pa.DataFrameModel):
    """
    Classe para o schema ItensPedidos que herda a validação do pandera Schema Model

    item_pedido_id: Inteiros Positivos
    pedido_id: Inteiros Positivos
    produto_id: Inteiros Positivos
    quantidade: Inteiros Não Negativo
    preco_unitario: Float não Negativo

    Config:
    coerce: converte os dados para os tipos definidos
    strict: exige que o dataframe tenha as mesmas colunas do schema
    """
    item_pedido_id : Series[int] = pa.Field(gt = 0)
    pedido_id : Series[int] = pa.Field(gt = 0)
    produto_id : Series[int] = pa.Field(gt = 0)
    quantidade : Series[int] = pa.Field(ge = 0)
    preco_unitario : Series[float] = pa.Field(ge = 0)

    class Config:
        coerce = True
        strict = True
