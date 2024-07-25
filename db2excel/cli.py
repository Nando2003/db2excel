import argparse
from db2excel.postgresql import PostgreSQLToExcel
from db2excel.sqlite     import SqliteToExcel

def main():
    parser = argparse.ArgumentParser(description="Export database tables to Excel files.")
    parser.add_argument('db_type', choices=['postgresql', 'sqlite'], help="Type of database")
    parser.add_argument('--database', help="Database name")
    parser.add_argument('--username', help="Database username")
    parser.add_argument('--password', help="Database password")
    parser.add_argument('--host', help="Database host")
    parser.add_argument('--port', type=int, help="Database port")
    parser.add_argument('--db_path', help="Path to SQLite database file")
    parser.add_argument('--download_path', required=True, help="Path to save Excel files")
    parser.add_argument('--excel_name', help="Name of the Excel file")
    parser.add_argument('--overwrite', action='store_true', help="Overwrite existing files")

    args = parser.parse_args()

    if args.db_type == 'postgresql':
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
        exporter = SqliteToExcel(
            db_path=args.db_path,
            download_path=args.download_path,
            excel_name=args.excel_name,
            overwrite=args.overwrite
        )

if __name__ == "__main__":
    main()
