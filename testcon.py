from ftputil import FTPHost
import psycopg2

# # def check_ftp_connection(ftp_host, ftp_user, ftp_password, ftp_remote_folder):
# #     try:
# #         # Attempt to establish a connection to the FTP server
# #         with FTPHost(ftp_host, ftp_user, ftp_password) as ftp:
# #             # Check if the remote folder exists
# #             if ftp_remote_folder in ftp.listdir(ftp_remote_folder):
# #                 print("FTP Connection Successful")
# #             else:
# #                 print(f"FTP Connection Successful, but {ftp_remote_folder} not found")
# #     except Exception as e:
# #         print(f"FTP Connection Failed: {e}")

# def check_postgres_connection(pg_host, pg_database, pg_user, pg_password,pg_port):
#     try:
#         # Attempt to establish a connection to PostgreSQL
#         with psycopg2.connect(
#             host=pg_host,
#             database=pg_database,
#             user=pg_user,
#             password=pg_password,
#             port=pg_port
#         ) as conn:
#             print("PostgreSQL Connection Successful")
#     except Exception as e:
#         print(f"PostgreSQL Connection Failed: {e}")

# #Example usage:
# # ftp_host = 'order.kacoldstorage.com'
# # ftp_user = 'c011'
# # ftp_password = '110c'
# # ftp_remote_folder = 'Report'

# pg_host = '192.168.0.21'
# pg_database = 'ubuntu1_cedea'
# pg_user = 'postgres'
# pg_password = 'iTc3D3A24#24'
# pg_port = '5432'




# # check_ftp_connection(ftp_host, ftp_user, ftp_password, ftp_remote_folder)
# check_postgres_connection(pg_host, pg_database, pg_user, pg_password, pg_port)


# ================== success ======================
# import psycopg2

# # Replace these with your database connection details
# dbname = "wms_legacy"
# user = "postgres"
# password = "iTc3D3A24#24"
# host = "192.168.0.21"  # For local development, use "localhost"
# port = "5432"  # Default PostgreSQL port is 5432
# table_name = "stock_ka_location_history"

# try:
#     # Establish a connection to the PostgreSQL database
#     connection = psycopg2.connect(
#         dbname=dbname,
#         user=user,
#         password=password,
#         host=host,
#         port=port
#     )

#     # Create a cursor object to interact with the database
#     cursor = connection.cursor()

#     # Execute a SELECT query on the specified table
#     query = f"SELECT * FROM {table_name};"
#     cursor.execute(query)

#     # Fetch all rows from the result set
#     rows = cursor.fetchall()

#     # Print the column names
#     column_names = [desc[0] for desc in cursor.description]
#     print(column_names)

#     # Print each row
#     for row in rows:
#         print(row)

# except (Exception, psycopg2.Error) as error:
#     print("Error while connecting to PostgreSQL:", error)

# finally:
#     # Close the cursor and connection
#     if connection:
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")
        
        
# =================================================================
        
        
# import psycopg2

# # Replace these with your database connection details
# dbname = "Belajar"
# user = "postgres"
# password = "pgsql"
# host = "localhost"  # For local development, use "localhost"
# port = "5432"  # Default PostgreSQL port is 5432

# # pg_host = 'localhost'
# # pg_database = 'soh_master'
# # pg_user = 'postgres'
# # pg_password = 'pgsql'
# # pg_port = '5432'

# try:
#     # Establish a connection to the PostgreSQL database
#     connection = psycopg2.connect(
#         dbname=dbname,
#         user=user,
#         password=password,
#         host=host,
#         port=port
#     )

#     # Create a cursor object to interact with the database
#     cursor = connection.cursor()

#     # Execute SQL queries here using cursor.execute()

#     # Example: cursor.execute("SELECT * FROM your_table")
#     #           result = cursor.fetchall()
#     #           print(result)

# except (Exception, psycopg2.Error) as error:
#     print("Error while connecting to PostgreSQL:", error)

# finally:
#     # Close the cursor and connection
#     if connection:
#         # cursor.close()
#         # connection.close()
#         print("PostgreSQL connection ")




