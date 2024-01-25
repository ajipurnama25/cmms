import pandas as pd
import psycopg2
from ftputil import FTPHost
from io import BytesIO
import schedule
import time
import os
import re
import testcon

file_names = ['STOCKM_C011_20210116.xlsx', 'STOCKM_C011_20210123.xlsx']
# extract date form soh file
def extract_date_from_filename(file_name):
    match = re.search(r'_(\d{8})\.xlsx', file_name)
    if match:
        date_str = match.group(1)
        return pd.to_datetime(date_str, format='%Y%m%d')
    else:
        return None
    
def get_soh_ftp_dates(remote_path):
    # Membuat koneksi ke database PostgreSQL
    ftp = FTPHost(testcon.ftp_host, testcon.ftp_user, testcon.ftp_password)

    # Mendapatkan daftar file di folder FTP
    ftp_files = ftp.listdir(testcon.ftp_remote_folder)
    
    # Pandas df
    df = pd.DataFrame()
    
    for file_name in ftp_files:
        date = extract_date_from_filename(file_name)
        print(f"File: {file_name}, Date: {date}")
    
    df = df.append({'File': file_name, 'Date': date}, ignore_index=True)
    
    ftp.close()
    return(df)
    

# query distinct tgl_import date from locaton history
def get_soh_postgres_dates():
    # Query postgres import dates in location history
    query = "select distinct cast(tgl_import as date) as import_date from stock_ka_location_history"
    
    df = pd.read_sql_query(query, testcon.pg_conn)

    # Return dates
    return(df)



def update_postgresql_from_ftp(ftp, remote_path, conn):
    with ftp.open(remote_path, 'rb') as remote_file:
        # Membaca data dari file Excel yang ada di FTP langsung ke DataFrame
        df = pd.read_excel(BytesIO(remote_file.read()))

        # Menambahkan data baru ke PostgreSQL
        df.to_sql('stock_ka_location_history', conn, if_exists='append', index=False)

def job():
    ftp_host = 'order.kacoldstorage.com'
    ftp_user = 'c011'
    ftp_password = '110c'
    ftp_remote_folder = 'Report/1 SOH'

    pg_conn = psycopg2.connect(
        host='192.168.0.21',
        database='ubuntu1_cedea',
        user='postgres',
        password='iTc3D3A24#24'
    )
    
    # Membuat koneksi ke database PostgreSQL
    ftp = FTPHost(testcon.ftp_host, testcon.ftp_user, testcon.ftp_password)

    # Mendapatkan daftar file di folder FTP
    ftp_files = ftp.listdir(testcon.ftp_remote_folder)

    for ftp_file in ftp_files:
        remote_path = os.path.join(testcon.ftp_remote_folder, ftp_file)
        print(ftp_file)
        # Memperbarui PostgreSQL dari file Excel di FTP
        update_postgresql_from_ftp(ftp, remote_path, testcon)
        
        print(ftp_file)

    # Menutup koneksi
    testcon.pg_conn.close()

# Menjadwalkan pembaruan setiap 1 jam
schedule.every().hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
