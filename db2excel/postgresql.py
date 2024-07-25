from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.engine.base import Engine
from typing import Union

from .base import DatabaseToExcel

class PostgreSQLToExcel(DatabaseToExcel):

    def __init__(
        self,
        database      :str,
        username      :str,
        password      :str,
        host          :str,
        port          :Union[str, int],
        download_path :str,
        excel_name    :str  = None,
        overwrite     :bool = False
    ):
        super().__init__(
            database      = database,
            username      = username,
            password      = password,
            host          = host,
            port          = port,
            download_path = download_path,
            excel_name    = excel_name,
            overwrite     = overwrite
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
