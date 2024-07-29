from ._base import DatabaseToExcel

from sqlalchemy.engine.base import Engine
from sqlalchemy import create_engine, text

class SqliteToExcel(DatabaseToExcel):
    def __init__(
        self, 
        db_path:str, 
        download_path:str, 
        excel_name:str= None, 
        overwrite:bool= False
    ):
        self.db_path = db_path
        
        super().__init__(
            download_path = download_path,
            excel_name    =    excel_name,
            overwrite     =     overwrite,
        )
        
    def creating_engine(self) -> Engine:
        return create_engine(f'sqlite:///{self.db_path}')
    
    def search_all_the_data(self, columns: list, table_name: str) -> str:
        columns_name = ', '.join(f'"{col}"' for col in columns)
        return text(f'SELECT {columns_name} FROM "{table_name}"')