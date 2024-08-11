from pydantic import BaseModel, PositiveInt, EmailStr, PositiveFloat
from datetime import datetime
from typing import Literal


class Cliente(BaseModel):
    cliente_id : PositiveInt
    nome : str
    email : EmailStr
    data_cadastro : datetime

class Produtos(BaseModel):
    produto_id : PositiveInt
    nome : str
    categoria : Literal['Alimentos', 'Complementos', 'Bebidas', 'Snacks']
    preco : PositiveFloat

class Pedidos(BaseModel):
    pedido_id : PositiveInt
    cliente_id : PositiveInt
    data_pedido : datetime
    valor_total : PositiveFloat

class ItensPedido(BaseModel):
    item_pedido_id : PositiveInt
    pedido_id : PositiveInt
    produto_id : PositiveInt
    quantidade : PositiveInt
    preco_unitario : PositiveFloat