import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from src.extract import extract_csv_to_dataframe


@pytest.fixture
def exemplo_csv(tmp_path):
    """Cria um arquivo CSV temporário para os testes."""
    data = {'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']}
    df = pd.DataFrame(data)
    file_path = tmp_path / 'sample.csv'
    df.to_csv(file_path, index=False)
    return file_path


def test_extract_csv_to_dataframe_success(exemplo_csv):
    """Teste a função com um arquivo CSV válido."""
    df = extract_csv_to_dataframe(exemplo_csv)
    expected_df = pd.read_csv(exemplo_csv)
    assert df is not None
    assert_frame_equal(df, expected_df)


def test_extract_csv_to_dataframe_failure():
    """Teste a função com um arquivo CSV inválido."""
    invalid_file = 'non_existent_file.csv'
    df = extract_csv_to_dataframe(invalid_file)
    assert df is None
