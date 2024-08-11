from src.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy import func

class ClienteBase(Base):
    __tablename__ = 'clientes'

    cliente_id = Column(Integer, primary_key = True)
    nome = Column(String)
    email = Column(String)
    data_cadastro = Column(DateTime)
    created_at = Column(DateTime(timezone= True), default = func.now())

class ProdutosBase(Base):
    __tablename__ = 'produtos'

    produto_id = Column(Integer, primary_key= True)
    nome = Column(String)
    categoria = Column(String)
    preco = Column(Float)
    created_at = Column(DateTime(timezone= True), default = func.now())

class PedidosBase(Base):
    __tablename__ = 'pedidos'

    pedido_id = Column(Integer, primary_key= True)
    cliente_id = Column(Integer)
    data_pedido = Column(DateTime)
    valor_total = Column(Float)
    created_at = Column(DateTime(timezone= True), default = func.now())

class ItensPedidosBase(Base):
    item_pedido_id = Column(Integer, primary_key= True)
    pedido_id = Column(Integer)
    produto_id = Column(Integer)
    quantidade = Column(Integer)
    preco_unitario = Column(Float)
    created_at = Column(DateTime(timezone= True), default = func.now())