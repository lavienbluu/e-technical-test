import pandas as pd
from sqlalchemy import create_engine

# Specify the file paths for day1 data
item_referential_path = 'raw_data/day1_files/items.csv'
customer_referential_path = 'raw_data/day1_files/customers.csv'
order_header_path = 'raw_data/day1_files/order_headers.csv'
order_line_path = 'raw_data/day1_files/order_lines.csv'

# Load CSV files into pandas DataFrames
item_referential_df = pd.read_csv(item_referential_path)
customer_referential_df = pd.read_csv(customer_referential_path)
order_header_df = pd.read_csv(order_header_path)
order_line_df = pd.read_csv(order_line_path)

# Handling null values in customer_referential_df
customer_referential_df['postal_code'] = customer_referential_df['postal_code'].fillna('UNKNOWN')

# Ensuring length constraints in item_referential_df
item_referential_df['item_description'] = item_referential_df['item_description'].str[:50]
customer_referential_df['postal_code'] = customer_referential_df['postal_code'].str[:10]

order_header_df['order_date'] = pd.to_datetime(order_header_df['order_date'], format='%m/%d/%Y')
order_header_df['order_date'] = order_header_df['order_date'].dt.strftime('%Y-%m-%d')
order_line_df['ship_date'] = pd.to_datetime(order_line_df['ship_date'], format='%m/%d/%Y')
order_line_df['promise_date'] = pd.to_datetime(order_line_df['promise_date'], format='%m/%d/%Y')

# Display the first few rows of each DataFrame to verify the data
print("Item Referential Data:")
print(item_referential_df.head())

print("\nCustomer Referential Data:")
print(customer_referential_df.head())

print("\nOrder Header Data:")
print(order_header_df.head())

print("\nOrder Line Data:")
print(order_line_df.head())

# Database connection parameters
db_user = 'root'
db_password = '091016'
db_host = 'localhost'
db_port = '3306'
db_name = 'sales'

# Create a SQLAlchemy engine to connect to MariaDB
engine = create_engine(f'mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# Define table names
item_referential_table = 'item_referential'
customer_referential_table = 'customer_referential'
order_header_table = 'order_header'
order_line_table = 'order_line'

# Write DataFrames to MariaDB tables
item_referential_df.to_sql(name=item_referential_table, con=engine, index=False, if_exists='append')
customer_referential_df.to_sql(name=customer_referential_table, con=engine, index=False, if_exists='append')
order_header_df.to_sql(name=order_header_table, con=engine, index=False, if_exists='append')
order_line_df.to_sql(name=order_line_table, con=engine, index=False, if_exists='append')

# Close the database connection
engine.dispose()

print("Data loaded into MariaDB tables successfully!")