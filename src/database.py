from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# URL de conexão com o PostgreSQL, formada a partir das variáveis de ambiente
DB_HOST = 'dpg-cqtusiogph6c73a5s900-a.oregon-postgres.render.com'
DB_PORT = '5432'
DB_NAME = 'db_the_best'
DB_USER = 'user'
DB_PASSWORD = 'MioJINC0OznxHQQyXLhUH5pwXWYR9bbw'

POSTGRES_DATABASE_URL = (
    f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)

# Criação da Engine
# Ela é responsável por gerenciar a conexão e executar comandos SQL.
engine = create_engine(POSTGRES_DATABASE_URL)

# Criação da SessionLocal: SessionLocal é uma fábrica de sessões para interagir com o banco de dados.
# Cada sessão é uma transação com o banco e é usada para enviar e consultar dados.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criação da Base: Base é a classe base para todas as classes de modelo (ou tabelas) do SQLAlchemy.
# Ela é usada para mapear as classes Python para tabelas no banco de dados.
Base = declarative_base()
