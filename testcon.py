from ftputil import FTPHost
import psycopg2

# def check_ftp_connection(ftp_host, ftp_user, ftp_password, ftp_remote_folder):
#     try:
#         # Attempt to establish a connection to the FTP server
#         with FTPHost(ftp_host, ftp_user, ftp_password) as ftp:
#             # Check if the remote folder exists
#             if ftp_remote_folder in ftp.listdir(ftp_remote_folder):
#                 print("FTP Connection Successful")
#             else:
#                 print(f"FTP Connection Successful, but {ftp_remote_folder} not found")
#     except Exception as e:
#         print(f"FTP Connection Failed: {e}")

def check_postgres_connection(pg_host, pg_database, pg_user, pg_password,pg_port):
    try:
        # Attempt to establish a connection to PostgreSQL
        with psycopg2.connect(
            host=pg_host,
            database=pg_database,
            user=pg_user,
            password=pg_password,
            port=pg_port
        ) as conn:
            print("PostgreSQL Connection Successful")
    except Exception as e:
        print(f"PostgreSQL Connection Failed: {e}")

#Example usage:
# ftp_host = 'order.kacoldstorage.com'
# ftp_user = 'c011'
# ftp_password = '110c'
# ftp_remote_folder = 'Report'

pg_host = '192.168.0.21'
pg_database = 'ubuntu1_cedea'
pg_user = 'postgres'
pg_password = 'iTc3D3A24#24'
pg_port = '5432'




# check_ftp_connection(ftp_host, ftp_user, ftp_password, ftp_remote_folder)
check_postgres_connection(pg_host, pg_database, pg_user, pg_password, pg_port)



