import sqlite3
import random
import string
import os

def create_connection(db_file):
    """
    Cria uma conexão com o banco de dados SQLite especificado.
    
    Args:
        db_file (str): O caminho para o arquivo do banco de dados SQLite.
    
    Returns:
        sqlite3.Connection: Objeto de conexão com o banco de dados.
    """
    conn = sqlite3.connect(db_file)
    return conn

def generate_random_table_name():
    """
    Gera um nome de tabela aleatório com 8 caracteres.
    
    Returns:
        str: Nome da tabela.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def create_table(conn, table_name):
    """
    Cria uma tabela com o nome especificado no banco de dados.
    
    Args:
        conn (sqlite3.Connection): Objeto de conexão com o banco de dados.
        table_name (str): Nome da tabela a ser criada.
    """
    try:
        sql_create_table = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_table)
        conn.commit()
        print(f"Tabela '{table_name}' criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela: {e}")

def insert_random_data(conn, table_name, num_records):
    """
    Insere um número especificado de registros aleatórios na tabela.
    
    Args:
        conn (sqlite3.Connection): Objeto de conexão com o banco de dados.
        table_name (str): Nome da tabela onde os dados serão inseridos.
        num_records (int): Número de registros a serem inseridos.
    """
    try:
        sql_insert = f"INSERT INTO {table_name} (name, age) VALUES (?, ?);"
        cursor = conn.cursor()
        
        for _ in range(num_records):
            name = ''.join(random.choices(string.ascii_letters, k=5))
            age = random.randint(18, 99)
            cursor.execute(sql_insert, (name, age))
        
        conn.commit()
        print(f"{num_records} registros inseridos na tabela '{table_name}'.")
    except sqlite3.Error as e:
        print(f"Erro ao inserir dados: {e}")

def query_data(conn, table_name):
    """
    Consulta todos os registros da tabela especificada e imprime os resultados.
    
    Args:
        conn (sqlite3.Connection): Objeto de conexão com o banco de dados.
        table_name (str): Nome da tabela a ser consultada.
    """
    try:
        sql_query = f"SELECT * FROM {table_name};"
        cursor = conn.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        
        print(f"Dados da tabela '{table_name}':")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"Erro ao consultar dados: {e}")

def main():
    database = f"{os.path.dirname(__file__)}/sqlite3.db"  # Nome do arquivo do banco de dados SQLite

    # Cria uma conexão com o banco de dados
    conn = create_connection(database)
    
    if conn:
        # Gera um nome de tabela aleatório
        table_name = generate_random_table_name()
        
        # Cria a tabela
        create_table(conn, table_name)
        
        # Insere dados aleatórios na tabela
        insert_random_data(conn, table_name, 10)  # Insere 10 registros aleatórios
        
        # Consulta e imprime os dados
        query_data(conn, table_name)
        
        # Fecha a conexão
        conn.close()

if __name__ == "__main__":
    main()
