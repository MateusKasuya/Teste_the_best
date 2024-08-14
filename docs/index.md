# API Documentation

Abaixo, você encontrará detalhes sobre as funções e módulos do projeto.

## Módulo `etl`

### `extract`

```python
def extract_csv_to_dataframe(file_csv: str) -> pd.DataFrame:
    """
    Essa função tem o objetivo de ler arquivos CSV e salvar em um DataFrame Pandas.

    Args:
        file_csv (str): Caminho do arquivo CSV.

    Returns:
        pd.DataFrame: DataFrame Pandas contendo os dados do arquivo CSV.
    """
```

### `schema`

```python
class ClientesSchema(pa.DataFrameModel):
    """
    Classe para o schema Cliente que herda a validação do Pandera Schema Model.

    Attributes:
        cliente_id (int): Inteiros Positivos.
        nome (str): Nome do cliente.
        email (str): Email validado pela variável regex `email_regex`.
        data_cadastro (datetime): Data e hora do cadastro.

    Config:
        coerce: Converte os dados para os tipos definidos.
        strict: Exige que o DataFrame tenha as mesmas colunas do schema.
    """
 ```   

### `transform`

```python
@pa.check_output(ClientesSchema, lazy=True)
def transform_clientes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Essa função recebe um DataFrame e realiza as tratativas adequadas:
    - Garante que as tabelas possuam chaves primárias únicas.
    - Garante que as colunas de data sejam transformadas no formato correto.
    - Transforma as colunas numéricas de quantidade e valores sempre em números positivos.

    Args:
        df (pd.DataFrame): DataFrame contendo os dados a serem transformados.

    Returns:
        pd.DataFrame: DataFrame transformado conforme as regras definidas.
    """
```

### `database`

```python
# Criação da Engine
# Responsável por gerenciar a conexão e executar comandos SQL.
engine = create_engine(POSTGRES_DATABASE_URL)

# Criação da SessionLocal: Fábrica de sessões para interagir com o banco de dados.
# Cada sessão é uma transação com o banco e é usada para enviar e consultar dados.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criação da Base: Classe base para todas as classes de modelo (ou tabelas) do SQLAlchemy.
# Usada para mapear as classes Python para tabelas no banco de dados.
Base = declarative_base()
```

### `models`

```python
class ClienteBase(Base):
    __tablename__ = 'clientes'

    cliente_id = Column(Integer, primary_key=True)  # Identificador único do cliente, chave primária
    nome = Column(String)
    email = Column(String)
    data_cadastro = Column(DateTime)
    created_at = Column(DateTime(timezone=True), default=func.now())  # Data e hora de criação do registro, com timezone
```

### `load`

```python
def load_dataframe_to_postgres(df: pd.DataFrame, model, session: Session):
    """
    Essa função carrega os dados de um DataFrame para a tabela correspondente no banco de dados Postgres,
    substituindo os dados existentes.

    Args:
        df (pd.DataFrame): DataFrame que contém os dados a serem carregados.
        model (Base): Classe de modelo correspondente à tabela do banco de dados.
        session (Session): Sessão do SQLAlchemy para interação com o banco de dados.
    """
```

### `main`

```python
def run_etl():
    """
    Função principal que executa o pipeline ETL:
    - Cria as tabelas no banco de dados.
    - Realiza a extração dos arquivos CSV.
    - Aplica a transformação nos DataFrames.
    - Carrega os dados transformados no banco de dados.
    """
    Base.metadata.create_all(engine)

    session = SessionLocal()

    # Caminhos dos arquivos CSV
    clientes_csv = 'data/clientes 2(in).csv'
    produtos_csv = 'data/produtos 2(in).csv'
    pedidos_csv = 'data/pedidos 2(in).csv'
    itenspedido_csv = 'data/itens_pedido 2(in).csv'

    # Realiza a extração dos arquivos
    clientes_df = extract_csv_to_dataframe(clientes_csv)
    produtos_df = extract_csv_to_dataframe(produtos_csv)
    pedidos_df = extract_csv_to_dataframe(pedidos_csv)
    itenspedido_df = extract_csv_to_dataframe(itenspedido_csv)

    # Aplica a transformação nos DataFrames
    clientes_df_transformed = transform_clientes(clientes_df)
    produtos_df_transformed = transform_produtos(produtos_df)
    pedidos_df_transformed = transform_pedidos(pedidos_df)
    itenspedido_df_transformed = transform_itenspedidos(itenspedido_df)

    # Carrega os dados no banco de dados
    load_dataframe_to_postgres(clientes_df_transformed, ClienteBase, session)
    load_dataframe_to_postgres(produtos_df_transformed, ProdutosBase, session)
    load_dataframe_to_postgres(pedidos_df_transformed, PedidosBase, session)
    load_dataframe_to_postgres(itenspedido_df_transformed, ItensPedidosBase, session)


if __name__ == '__main__':
    run_etl()
```
