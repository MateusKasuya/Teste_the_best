# Dockerfile

# Imagem base
FROM python:3.9

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar o arquivo de requisitos do diretório raiz
COPY ../requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copiar o restante dos arquivos do projeto
COPY . /app

# Instalar dependências adicionais para pandas e SQLAlchemy
RUN pip install --no-cache-dir pandas sqlalchemy psycopg2-binary pandera

# Comando para executar o script Python
CMD ["python", "main.py"]
