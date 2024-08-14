import pandas as pd
from sqlalchemy import text
from sqlalchemy.orm import Session


def load_dataframe_to_postgres(df: pd.DataFrame, model, session: Session):
    """
    Essa função carrega os dados de um DataFrame para a tabela correspondente no banco de dados Postgres,
    substituindo os dados existentes.

    df -> DataFrame que contém os dados a serem carregados.
    model -> Classe de modelo correspondente à tabela do banco de dados.
    session -> Sessão do SQLAlchemy para interação com o banco de dados.
    """
    try:
        # Exclui todos os dados existentes na tabela
        session.execute(text(f'DELETE FROM {model.__tablename__}'))
        session.commit()

        # Converte o DataFrame para uma lista de dicionários
        data_to_insert = df.to_dict(orient='records')

        # Usa a função bulk_insert_mappings para inserir os dados
        session.bulk_insert_mappings(model, data_to_insert)
        session.commit()
        print(f'Dados carregados com sucesso na tabela {model.__tablename__}.')
    except Exception as e:
        session.rollback()
        print(
            f'Erro ao carregar dados para a tabela {model.__tablename__}: {e}'
        )
    finally:
        session.close()
