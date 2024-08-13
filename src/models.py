from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import relationship

from database import Base


# Define a tabela 'clientes' no banco de dados
class ClienteBase(Base):
    __tablename__ = 'clientes'

    cliente_id = Column(
        Integer, primary_key=True
    )  # Identificador único do cliente, chave primária
    nome = Column(String)
    email = Column(String)
    data_cadastro = Column(DateTime)
    created_at = Column(
        DateTime(timezone=True), default=func.now()
    )  # Data e hora em que o registro foi criado, com timezone


# Define a tabela 'produtos' no banco de dados
class ProdutosBase(Base):
    __tablename__ = 'produtos'

    produto_id = Column(
        Integer, primary_key=True
    )  # Identificador único do produto, chave primária
    nome = Column(String)
    categoria = Column(String)
    preco = Column(Float)
    created_at = Column(
        DateTime(timezone=True), default=func.now()
    )  # Data e hora em que o registro foi criado, com timezone


# Define a tabela 'pedidos' no banco de dados
class PedidosBase(Base):
    __tablename__ = 'pedidos'

    pedido_id = Column(
        Integer, primary_key=True
    )  # Identificador único do pedido, chave primária
    cliente_id = Column(
        Integer, ForeignKey('clientes.cliente_id')
    )  # Chave estrangeira para 'clientes'
    data_pedido = Column(DateTime)
    valor_total = Column(Float)
    created_at = Column(
        DateTime(timezone=True), default=func.now()
    )  # Data e hora em que o registro foi criado, com timezone

    # Define o relacionamento com a tabela 'clientes'
    cliente = relationship('ClienteBase')


# Define a tabela 'itens_pedidos' no banco de dados
class ItensPedidosBase(Base):
    __tablename__ = 'itens_pedidos'

    item_pedido_id = Column(
        Integer, primary_key=True
    )  # Identificador único do item do pedido, chave primária
    pedido_id = Column(
        Integer, ForeignKey('pedidos.pedido_id')
    )  # Chave estrangeira para 'pedidos'
    produto_id = Column(
        Integer, ForeignKey('produtos.produto_id')
    )  # Chave estrangeira para 'produtos'
    quantidade = Column(Integer)
    preco_unitario = Column(Float)
    created_at = Column(
        DateTime(timezone=True), default=func.now()
    )  # Data e hora em que o registro foi criado, com timezone

    # Define os relacionamentos com as tabelas 'pedidos' e 'produtos'
    pedido = relationship('PedidosBase')
    produto = relationship('ProdutosBase')
