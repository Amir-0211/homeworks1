import os
import pandas as pd
import pyodbc
import logging

# Database connection configuration (Windows Authentication)
DB_SERVER = r'AMIRBEK\SQLEXPRESS01'  # Your SQL Server instance
DB_DATABASE = 'Python'  # Your database name

# Updated files to process
FILES_TO_PROCESS = [
    r"C:\Source folder\industry.csv",
    r"C:\Source folder\industry_sic.csv"
]

# Configure logging
LOG_FILE = 'etl_process.log'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_db_connection():
    """Establish a connection to the SQL Server database using Windows Authentication."""
    try:
        conn_str = f'DRIVER={{SQL Server}};SERVER={DB_SERVER};DATABASE={DB_DATABASE};Trusted_Connection=yes;'
        return pyodbc.connect(conn_str)
    except Exception as e:
        logging.error(f"Failed to connect to the database: {e}")
        raise

def process_csv(file_path, table_name, connection):
    """Processes a CSV file and loads it into the database."""
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Processing file: {file_path}")
        
        with connection.cursor() as cursor:
            # Drop table if it exists
            cursor.execute(f"IF OBJECT_ID('{table_name}', 'U') IS NOT NULL DROP TABLE {table_name}")
            connection.commit()

            # Create table dynamically
            columns = ', '.join([f"[{col}] NVARCHAR(MAX)" for col in df.columns])
            create_table_query = f"CREATE TABLE {table_name} ({columns})"
            cursor.execute(create_table_query)
            connection.commit()

            # Insert data into the table
            for _, row in df.iterrows():
                placeholders = ', '.join(['?'] * len(row))
                insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
                cursor.execute(insert_query, tuple(row))
            connection.commit()
        
        logging.info(f"File {file_path} successfully loaded into table {table_name}.")
    except Exception as e:
        logging.error(f"Error processing file {file_path}: {e}")
        raise

def main():
    """Main ETL process."""
    connection = get_db_connection()
    try:
        for file_path in FILES_TO_PROCESS:
            if os.path.exists(file_path) and file_path.endswith('.csv'):
                table_name = os.path.splitext(os.path.basename(file_path))[0]  # Use file name as table name
                process_csv(file_path, table_name, connection)
        logging.info("ETL process completed successfully.")
    except Exception as e:
        logging.error(f"ETL process failed: {e}")
    finally:
        connection.close()

if __name__ == "__main__":
    main()
