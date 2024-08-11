import pandera as pa
from pandera.typing import DataFrame, Series
import pandas as pd

email_regex = r"[^@]+@[^@]+\.[^@]+"

class Cliente(pa.SchemaModel):
    cliente_id : Series[int] = pa.Field(gt = 0)
    nome : Series[str]
    email : Series[str] = pa.Field(regex = email_regex)
    data_cadastro  : Series[pd.Timestamp] = pa.Field()

    class Config:
        coerce = True
        strict = True

CATEGORIAS_PERMITIDAS = ['Alimentos', 'Complementos', 'Bebidas', 'Snacks']

class Produtos(pa.SchemaModel):
    produto_id : Series[int] = pa.Field(gt = 0)
    nome : Series[str]
    categoria : Series[str] = pa.Field(check = pa.Check(lambda x: x.isin(CATEGORIAS_PERMITIDAS)))
    preco : Series[float] = pa.Field(gt = 0)

    class Config:
        coerce = True
        strict = True

class Pedidos(pa.SchemaModel):
    pedido_id : Series[int] = pa.Field(gt = 0)
    cliente_id : Series[int] = pa.Field(gt = 0)
    data_pedido : Series[pd.Timestamp] = pa.Field()
    valor_total : Series[float] = pa.Field(gt = 0)

    class Config:
        coerce = True
        strict = True

class ItensPedido(pa.SchemaModel):
    item_pedido_id : Series[int] = pa.Field(gt = 0)
    pedido_id : Series[int] = pa.Field(gt = 0)
    produto_id : Series[int] = pa.Field(gt = 0)
    quantidade : Series[int] = pa.Field(gt = 0)
    preco_unitario : Series[float] = pa.Field(gt = 0)
