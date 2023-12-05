import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError

# Function to check for primary key violations
def check_primary_key_violations(df, table_name, engine):
    primary_key_column = df.columns[0]  # Assuming the primary key is the first column
    existing_ids_query = f"SELECT {primary_key_column} FROM {table_name} WHERE {primary_key_column} IN ({','.join(map(str, df[primary_key_column].tolist()))})"
    existing_ids = pd.read_sql_query(existing_ids_query, engine)

    duplicate_ids = df[df.duplicated(subset=[primary_key_column], keep=False)]

    conflicting_ids = set(existing_ids[primary_key_column].tolist()) & set(duplicate_ids[primary_key_column].tolist())
    non_conflicting_ids = set(df[primary_key_column].tolist()) - conflicting_ids

    return primary_key_column, conflicting_ids, non_conflicting_ids

# Function to update data when there's a conflict
def update_item_data(new_data, table_name, primary_key_column, connection):
    # Construct the UPDATE query to update non-primary key columns
    update_query = f"UPDATE {table_name} SET "
    update_columns = []

    for col in new_data.columns:
        if col != primary_key_column:
            update_columns.append(f"{col} = '{new_data[col].iloc[0]}'")

    update_query += ', '.join(update_columns)
    update_query += f" WHERE {primary_key_column} = {new_data[primary_key_column].iloc[0]}"

    # Execute the UPDATE query
    connection.execute(update_query)

# Function to insert non-conflicting data
def insert_non_conflicting_data(df, table_name, primary_key_column, connection):
    # Ensure explicit column names in the DataFrame
    df.columns = [str(col) for col in df.columns]

    # Specify if_exists and index parameters in the to_sql method
    for _, row in df.iterrows():
        try:
            # Include the primary key column in the insert statement
            row.to_sql(name=table_name, con=connection, if_exists='append', index=False, method='multi', chunksize=1000)
        except IntegrityError:
            # Handle IntegrityError (e.g., log the error, skip the row, etc.)
            print(f"IntegrityError: Skipping duplicate entry for {primary_key_column} = {row[primary_key_column]}")

# Write DataFrames to MariaDB tables with conflict resolution
def write_to_sql_with_conflict_resolution(df, table_name, engine, primary_key_column):
    connection = engine.connect()
    try:
        # Try to append the data to the table
        df.to_sql(name=table_name, con=engine, index=False, if_exists='append')

    except IntegrityError as e:
        # Handle IntegrityError (e.g., log the error, skip the row, etc.)
        print(f"IntegrityError: {e}")

        # Identify conflicting rows
        conflicting_rows = pd.merge(df, pd.read_sql_query(f"SELECT {primary_key_column} FROM {table_name}", engine),
                                     how='inner', on=primary_key_column)

        # Update conflicting rows
        for _, row in conflicting_rows.iterrows():
            update_item_data(row, table_name, primary_key_column, connection)

    finally:
        connection.close()

# Define your MariaDB connection string
db_username = 'your_username'
db_password = 'your_password'
db_host = 'your_host'
db_port = 'your_port'
db_name = 'your_database_name'

# Create an SQLAlchemy engine
engine = create_engine(f"mysql+mysqldb://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}")

# Sample DataFrames (replace these with your actual DataFrames)
item_referential_df = pd.DataFrame({
    'item_id': [1, 2, 3, 4, 5],
    'item_description': ['OCTINOXATE and TITANIUM DIOXIDE', 'medroxyprogesterone acetate', 'Progesterone',
                          'penicillin G potassium', 'Corn, Cultivated Zea mays'],
    'item_status': ['N', 'N', 'Y', 'N', 'Y']
})

# Sample usage of the write_to_sql_with_conflict_resolution function
item_referential_table = 'item_referential'
write_to_sql_with_conflict_resolution(item_referential_df, item_referential_table, engine, 'item_id')

# ... (repeat for other DataFrames and tables)

# Close the database connection
engine.dispose()

print("Data loaded into MariaDB tables successfully!")