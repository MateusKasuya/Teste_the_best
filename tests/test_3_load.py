import pandas as pd
import pytest
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.load import load_dataframe_to_postgres

# URL de conexão com o PostgreSQL, formada a partir das variáveis de ambiente
DB_HOST = 'dpg-cqtusiogph6c73a5s900-a.oregon-postgres.render.com'
DB_PORT = '5432'
DB_NAME = 'db_the_best'
DB_USER = 'user'
DB_PASSWORD = 'MioJINC0OznxHQQyXLhUH5pwXWYR9bbw'

POSTGRES_DATABASE_URL = (
    f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)

# Cria um engine e uma base
engine = create_engine(POSTGRES_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define um modelo de exemplo para testes
class TestModel(Base):
    __tablename__ = 'test_table'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    value = Column(Integer)


# Cria a tabela de teste
def setup_module(module):
    Base.metadata.create_all(bind=engine)


def teardown_module(module):
    Base.metadata.drop_all(bind=engine)


# Testa a função load_dataframe_to_postgres
def test_load_dataframe_to_postgres():
    # Cria um DataFrame de exemplo
    df = pd.DataFrame({'name': ['Alice', 'Bob'], 'value': [100, 200]})

    # Cria uma sessão de teste
    session = SessionLocal()

    try:
        # Chama a função para carregar dados
        load_dataframe_to_postgres(df, TestModel, session)

        # Verifica se os dados foram carregados corretamente
        result = session.query(TestModel).all()

        assert len(result) == 2
        assert result[0].name == 'Alice'
        assert result[1].value == 200

    finally:
        # Limpa os dados após os testes
        session.query(TestModel).delete()
        session.commit()
        session.close()
