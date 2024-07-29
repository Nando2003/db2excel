import pytest
import os
import sys

from sqlalchemy.engine.base import Engine
from sqlalchemy.sql.elements import TextClause

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib.db2excel.sqlite import SqliteToExcel

@pytest.fixture
def sqlite_to_excel():
    return SqliteToExcel(
        db_path=':memory:',
        download_path=None,
        excel_name=None,
        overwrite=False
    )

def test_creating_engine(sqlite_to_excel):
    engine = sqlite_to_excel.creating_engine()
    assert isinstance(engine, Engine)
    assert engine.url.drivername == 'sqlite'

def test_search_all_the_data(sqlite_to_excel):
    columns = ['id', 'name']
    table_name = 'users'
    query = sqlite_to_excel.search_all_the_data(columns, table_name)
    
    assert isinstance(query, TextClause)
    assert query.text =='SELECT "id", "name" FROM "users"', "A consulta SQL gerada está incorreta."