import pandas as pd
from sqlalchemy import create_engine
import os

def export_table_to_parquet(table_name, engine, output_directory):
    query = f"SELECT * FROM {table_name};"
    df = pd.read_sql_query(query, engine)
    
    # Define the output path for the Parquet file
    output_path = os.path.join(output_directory, f"{table_name}.parquet")
    
    # Save the DataFrame to Parquet format
    df.to_parquet(output_path, index=False, compression='snappy')
    
    print(f"Table {table_name} exported to {output_path} successfully!")

if __name__ == "__main__":
    # Replace these values with your database connection details
    db_config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': '091016',
        'database': 'dimensions'
    }

    # Replace 'path/to/your/parquet_files/' with the desired output directory
    output_directory = 'parquet_files'

    # Create an SQLAlchemy engine
    engine = create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}", echo=True)

    # Make sure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # List of tables in your data mart
    tables = ['items', 'orders', 'customers']

    # Export each table to Parquet
    for table_name in tables:
        export_table_to_parquet(table_name, engine, output_directory)

    # Close the database connection
    engine.dispose()

    print("All tables exported to Parquet files successfully!")