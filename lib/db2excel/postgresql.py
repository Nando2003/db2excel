from ._base import DatabaseToExcel
from typing import Union

from sqlalchemy import create_engine, text
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.url import URL

class PostgreSQLToExcel(DatabaseToExcel):
    
    def __init__(
        self,
        database         : str,
        username         : str,
        password         : str,
        host             : str,
        port             : Union[int, str],
        download_path    : str  = None,
        excel_name       : str  = None,
        overwrite        : bool = False,
    ):
        self.database = database
        self.username = username
        self.password = password
        self.host     =     host
        self.port     =     port
        
        super().__init__(
            download_path = download_path,
            excel_name    =    excel_name,
            overwrite     =     overwrite,
        )
        
    
    def creating_engine(self) -> Engine:
        db_url = {
            'database'  : self.database,
            'drivername': 'postgresql',
            'username'  : self.username,
            'password'  : self.password,
            'host'      : self.host,
            'port'      : self.port,
        }
        return create_engine(URL.create(**db_url))
    
    def search_all_the_data(self, columns: list, table_name: str) -> str:
        columns_name = ', '.join(f'"{col}"' for col in columns)
        return text(f'SELECT {columns_name} FROM "{table_name}"')