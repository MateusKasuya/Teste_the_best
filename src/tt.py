from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker

# URL de conexão com o PostgreSQL
POSTGRES_DATABASE_URL = 'postgresql://user:password@postgres/mydatabase'

# Criação da Engine
engine = create_engine(POSTGRES_DATABASE_URL)

# Criação da SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def test_connection():
    try:
        # Teste a conexão
        with engine.connect() as connection:
            print('Conexão com o banco de dados estabelecida com sucesso!')

        # Teste se podemos criar uma tabela
        from sqlalchemy import Column, Integer, MetaData, String, Table

        metadata = MetaData()
        test_table = Table(
            'test_table',
            metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String),
        )

        # Criação da tabela
        metadata.create_all(engine)
        print('Tabela de teste criada com sucesso!')

        # Verifica a existência da tabela
        with engine.connect() as connection:
            result = connection.execute(
                "SELECT table_name FROM information_schema.tables WHERE table_schema='public'"
            )
            tables = [row[0] for row in result]
            print('Tabelas no banco de dados:', tables)

    except OperationalError as e:
        print(f'Erro ao conectar ao banco de dados: {e}')
    except Exception as e:
        print(f'Erro inesperado: {e}')


if __name__ == '__main__':
    test_connection()
