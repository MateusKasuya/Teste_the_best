from sqlalchemy.orm import Session
from src.database import SessionLocal, engine
from src.models import ClienteBase, ProdutosBase, PedidosBase, ItensPedidosBase
import pandas as pd

def load_data_to_db(df: pd.DataFrame, model, session: Session):
    """
    Essa função carrega os dados de um DataFrame para a tabela correspondente no banco de dados.
    
    df -> DataFrame que contém os dados a serem carregados.
    model -> Classe de modelo correspondente à tabela do banco de dados.
    session -> Sessão do SQLAlchemy para interação com o banco de dados.
    """
    try:
        # Converte o DataFrame para uma lista de dicionários
        data_to_insert = df.to_dict(orient='records')

        # Usa a função bulk_insert_mappings para inserir os dados
        session.bulk_insert_mappings(model, data_to_insert)
        session.commit()
        print(f'Dados carregados com sucesso na tabela {model.__tablename__}.')
    except Exception as e:
        session.rollback()
        print(f"Erro ao carregar dados para a tabela {model.__tablename__}: {e}")
    finally:
        session.close()

