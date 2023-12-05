import pandas as pd
from sqlalchemy import create_engine

def export_table_to_parquet(table_name, engine, output_path):
    # Fetch data from the table using SQLAlchemy
    query = f"SELECT * FROM {table_name};"
    df = pd.read_sql_query(query, engine)

    # Save the DataFrame to Parquet format
    df.to_parquet(output_path, index=False, compression='snappy')
    print(f"Table {table_name} exported to {output_path} successfully!")

if __name__ == "__main__":
    # Connect to the MariaDB database
    db_config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': '091016',
        'database': 'dimensions'
    }

    # Replace 'your_username', 'your_password', and 'your_database' with your actual credentials
    engine = create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}", echo=True)

    # Define the output directory for Parquet files
    output_directory = '/parquet_files'

    # Define table names
    items_table = 'Items'
    customers_table = 'customers'
    orders_table = 'orders'

    # Export each table to Parquet
    export_table_to_parquet(items_table, engine, f"{output_directory}{items_table}.parquet")
    export_table_to_parquet(customers_table, engine, f"{output_directory}{customers_table}.parquet")
    export_table_to_parquet(orders_table, engine, f"{output_directory}{orders_table}.parquet")

    # Close the database connection
    engine.dispose()

    print("All tables exported to Parquet files successfully!")