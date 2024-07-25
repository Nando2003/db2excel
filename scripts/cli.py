import argparse

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from lib.db2excel.postgresql import PostgreSQLToExcel
from lib.db2excel.sqlite     import SqliteToExcel

def main():
    parser = argparse.ArgumentParser(description="Export database tables to an Excel file.")
    
    parser.add_argument('db_type', choices=['postgresql', 'sqlite'], help="The type of the database.")
    parser.add_argument('--database', help="The name of the database.")
    parser.add_argument('--username', help="The username for the database.")
    parser.add_argument('--password', help="The password for the database.")
    parser.add_argument('--host', help="The host of the database.")
    parser.add_argument('--port', help="The port of the database.")
    parser.add_argument('--db_path', help="The path to the SQLite database file.")
    parser.add_argument('--download_path', required=True, help="The path where the Excel file will be saved.")
    parser.add_argument('--excel_name', help="The name of the Excel file.")
    parser.add_argument('--overwrite', action='store_true', help="Whether to overwrite the existing Excel file.")
    
    args = parser.parse_args()

    if args.db_type == 'postgresql':
        if not all([args.database, args.username, args.password, args.host, args.port]):
            parser.error("Postgresql requires --database, --username, --password, --host, and --port.")
        
        exporter = PostgreSQLToExcel(
            database=args.database,
            username=args.username,
            password=args.password,
            host=args.host,
            port=args.port,
            download_path=args.download_path,
            excel_name=args.excel_name,
            overwrite=args.overwrite
        )
    elif args.db_type == 'sqlite':
        if not args.db_path:
            parser.error("SQLite requires --db_path.")
        
        exporter = SqliteToExcel(
            db_path=args.db_path,
            download_path=args.download_path,
            excel_name=args.excel_name,
            overwrite=args.overwrite
        )
    
    exporter._process()

if __name__ == '__main__':
    main()
