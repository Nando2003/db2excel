from .base import DatabaseToExcel
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

class SqliteToExcel(DatabaseToExcel):

    def __init__(
        self,
        db_path       :str,
        download_path :str,
        excel_name    :str=None,
        overwrite     :bool=False
    ):
        super().__init__(
            download_path = download_path,
            excel_name    = excel_name,
            overwrite     = overwrite
        )
        
        self.db_path = db_path

    def creating_engine(self) -> Engine:
        return create_engine(f'sqlite:///{self.db_path}')
