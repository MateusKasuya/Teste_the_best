from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Variáveis de ambiente
DB_USER = 'user'             # Nome de usuário para conectar ao banco de dados
DB_PASSWORD = 'password'     # Senha para conectar ao banco de dados
DB_HOST = 'postgres'         # Endereço do servidor do banco de dados (normalmente 'localhost' ou o IP do servidor)
DB_PORT = '5432'             # Porta padrão do PostgreSQL
DB_NAME = 'mydatabase'       # Nome do banco de dados ao qual conectar

# URL de conexão com o PostgreSQL, formada a partir das variáveis de ambiente
DATABASE_URL = (
    f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)

# Criação da Engine
# Ela é responsável por gerenciar a conexão e executar comandos SQL.
engine = create_engine(DATABASE_URL)

# Criação da SessionLocal: SessionLocal é uma fábrica de sessões para interagir com o banco de dados.
# Cada sessão é uma transação com o banco e é usada para enviar e consultar dados.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criação da Base: Base é a classe base para todas as classes de modelo (ou tabelas) do SQLAlchemy.
# Ela é usada para mapear as classes Python para tabelas no banco de dados.
Base = declarative_base()
