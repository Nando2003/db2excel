# **DB2EXCEL**

## *Description*

`db2excel` is a python package that permits extract data from a **relational database (MySQL, PostgreSQL, SQLite3)** to an **excel file (.xlsx)**.

## *Features*

- Supports multiple databases: **MySQL, PostgreSQL, SQLite**
- Extracts all tables and their data from the database
- Creates an Excel workbook with each table as a separate sheet
- Option to overwrite existing Excel files

## *Installation*

```bash
pip install git+https://github.com/Nando2003/db2excel.git
``` 

## *Usage*

To use the package, create an instance of the appropriate subclass for your database and specify the required parameters:

```python
from db2excel import PostgreSQLToExcel

exporter = PostgreSQLToExcel(
    database      = 'your_database',
    username      = 'your_username',
    password      = 'your_password',
    host          = 'localhost',
    port          = '5432',
    download_path = 'path/to/save',
    overwrite     = True
)
```

- **database (str):** Name of the database to export.
- **username (str):** Database user name.
- **password (str):** Database user password.
- **host (str):** Database host address.
- **port (str|int) :** Database port address.
- **download_path (str):** Directory to save the Excel file. If empty or None, saves in the current directory.
- **excel_name (str):** Name of the Excel file (without extension). Defaults to 'output'.
- **overwrite (bool):** If True, overwrites the existing file. Defaults to False.