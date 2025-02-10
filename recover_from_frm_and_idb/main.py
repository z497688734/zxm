import os
import subprocess
import mysql.connector

# 配置 MySQL 数据库连接信息
DB_USER = 'root'
DB_PASSWORD = ''
DB_HOST = '127.0.0.1'
DB_PORT = 3356
DB_NAME = 'my_test4'

# 需要处理的文件夹路径
DIRECTORY_PATH = "/Users/liuhaoyang/niuadmin"
DIRECTORY_MYSQL_DATA = "/Users/liuhaoyang/mysql56"

def connect_to_mysql():
    """连接到 MySQL 数据库并返回连接和游标"""
    conn = mysql.connector.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME
    )
    cursor = conn.cursor()
    return conn, cursor

def close_connection(conn, cursor):
    """关闭数据库连接"""
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def get_create_table_statement(frm_file):
    """使用 dbsake 解析 .frm 文件获取建表语句"""
    try:
        # 调用 dbsake 工具解析 FRM 文件并返回建表语句
        dump_command = ['dbsake', 'frmdump', frm_file]
        result = subprocess.check_output(dump_command, stderr=subprocess.STDOUT)
        create_table_sql = result.decode('utf-8').strip()
        return create_table_sql
    except subprocess.CalledProcessError as e:
        print(f"Error while executing dbsake: {e.output.decode('utf-8')}")
        return None

def restore_table(frm_file, ibd_file):
    """恢复表：解析 .frm 文件，创建表，导入 .ibd 文件"""
    table_name = os.path.splitext(os.path.basename(frm_file))[0]

    # 获取建表语句
    create_table_sql = get_create_table_statement(frm_file)
    if not create_table_sql:
        print(f"Failed to get create table SQL for {table_name}")
        return

    # 连接数据库并创建表
    conn, cursor = connect_to_mysql()
    try:
        # 执行建表语句
        cursor.execute(create_table_sql)
        print(f"Table {table_name} created.")

        # 执行 ALTER TABLE DISCARD TABLESPACE
        discard_sql = f"ALTER TABLE {table_name} DISCARD TABLESPACE;"
        cursor.execute(discard_sql)
        print(f"Table {table_name} discarded tablespace.")

        # 复制 IBD 文件到表所在的数据目录（假设 ibd 文件路径已经正确）
        copy_command = f"cp {ibd_file} {DIRECTORY_MYSQL_DATA}/{DB_NAME}/{table_name}.ibd"
        subprocess.run(copy_command, shell=True, check=True)
        print(f"IBD file for {table_name} copied.")

        # 执行 ALTER TABLE IMPORT TABLESPACE
        import_sql = f"ALTER TABLE {table_name} IMPORT TABLESPACE;"
        cursor.execute(import_sql)
        print(f"Table {table_name} imported tablespace successfully.")

    except mysql.connector.Error as err:
        print(f"Error with table {table_name}: {err}")

    finally:
        # 关闭连接
        close_connection(conn, cursor)

def process_files():
    """遍历文件夹，处理每个 FRM 和 IBD 文件"""
    for frm_file in os.listdir(DIRECTORY_PATH):
        if frm_file.endswith('.frm'):
            # 获取对应的 IBD 文件
            table_name = os.path.splitext(frm_file)[0]
            ibd_file = os.path.join(DIRECTORY_PATH, f"{table_name}.ibd")

            if os.path.exists(ibd_file):
                frm_file_path = os.path.join(DIRECTORY_PATH, frm_file)
                print(f"Processing {table_name}...")
                restore_table(frm_file_path, ibd_file)
            else:
                print(f"IBD file for table {table_name} does not exist, skipping.")


if __name__ == '__main__':
    process_files()