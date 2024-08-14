# Teste Técnico The Best

## Sobre o Projeto

Este repositório é uma parte do teste técnico do Grupo The Best. O intuito aqui é montar uma estrutura ETL em que se lê arquivos CSV e salva em um banco de dados Postgres.
### Abordagens do Projeto

* **Aplicar a estrutura padrão de projetos que eu gosto trabalhar**: Isso inclui a organização de diretórios, como o código-fonte, testes, documentação, entre outros.

* **Testes com Pytest**: Garantir que o código funcione como esperado, criando testes unitários e de integração.

* **Versionamento com Git e GitHub**: Versionar o projeto no GitHub para publicação.

* **Documentação com MKDocs**

* **Automatização e CI**: Configuração de rotinas de integração a qualidade do projeto.

* **Formatação de código**: Este projeto segue as normas da PEP8

## Começando

### Pré-requisitos

* **Pyenv**: É usado para gerenciar versões do Python. Utilizarei nesse projeto o Python 3.12.2.

* **Poetry**: Este projeto utiliza Poetry para gerenciamento de dependências.

### Instalação e Configuração

1. Clone o repositório:

```bash
git clone https://github.com/MateusKasuya/Teste_the_best
```

2. Configure a versão correta do Python com `pyenv`:

```bash
pyenv install 3.12.3
pyenv local 3.12.3
```

3. Configurar poetry para Python version 3.11.5 e ative o ambiente virtual:

```bash
poetry env use 3.12.3
poetry shell
```

4. Instale as dependencias do projeto:

```bash
poetry install
```

5. Execute os testes para garantir que tudo está funcionando como esperado:

```bash
task test
```

6. Execute o comando para ver a documentação do projeto:

```bash
task doc
http://127.0.0.1:8000/
```

7. Execute o comando de execucão da pipeline para realizar a ETL:

```bash
task run
```

8. Acesse uma ferramenta gerenciadora de banco de dados e coloque as variáveis de ambiente para conectar no banco postgres:
```bash
DB_HOST = 'dpg-cqtusiogph6c73a5s900-a.oregon-postgres.render.com'
DB_PORT = '5432'
DB_NAME = 'db_the_best'
DB_USER = 'user'
DB_PASSWORD = 'MioJINC0OznxHQQyXLhUH5pwXWYR9bbw'
```

9. Verifique as tabelas geradas:
```bash
select * from clientes;

select * from itens_pedidos;

select * from pedidos; 

select * from produtos;
```
## Contato

Para dúvidas, sugestões ou feedbacks:

* **Mateus Kasuya** - [mateusvbkasuya@gmail.com](mailto:mateusvbkasuya@gmail.com)
