import pandas as pd


def extract_csv_to_dataframe(file_csv: str) -> pd.DataFrame:
    """
    Essa função tem o objetivo de ler arquivos csv e salvar em um DataFrame Pandas

    file_csv -> Caminho do arquivo csv
    """

    try:
        df = pd.read_csv(file_csv, encoding='utf-8')
        print(f'Arquivo {file_csv} lido com sucesso.')
        return df

    except Exception as e:
        print(f'Erro ao carregar o arquivo {file_csv}: {e}')
        return None
