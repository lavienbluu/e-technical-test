# Technical Test with Essilor Done by Thanadon Pitakwarin

## Requirement Files
1. SQL script
2. Python script
3. Output file
4. Unit Test
5. Instruction to Execute

## Instruction
1. Create Database by using mariaDB
  * Paste dimensions.sql which in the SQL scripts folder to create dimensions database
  * Paste sales.sql which in the SQL scripts folder to create dimensions database

3. Paste all SQL scripts below to create a star schema in mariaDB in the query box of database
  * Run audit_table.sql which in the SQL scripts folder
  * Run customer_referential.sql which in the SQL scripts folder
  * Run items_referential.sql which in the SQL scripts folder
  * Run order_header.sql which in the SQL scripts folder
  * Run order_lines.sql which in the SQL scripts folder

4. Paste all SQL scripts below to create a data mart in the mariaDB in the query box of database
  * Run dimensions.customers.sql which in the SQL scripts folder
  * Run dimensions.items.sql which in the SQL scripts folder
  * Run dimensions.orders.sql which in the SQL scripts folder
  * Run sales.salehistory.sql which in the SQL scripts folder

5. Run a Python script in VSCode to upload day1 and day2 to database
  * Run batch_ingestion_day1.py
  * Run batch_ingestion_day2.py

6. The output files are in parquet_files folder by
  * Run export_to_parquet_dimensions.py
  * Run export_to_parquet_sales.py
