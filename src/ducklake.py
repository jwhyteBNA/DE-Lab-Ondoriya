import os
import duckdb
from dotenv import load_dotenv
from minio import Minio

load_dotenv()

MINIO_EXTERNAL_URL = os.getenv('MINIO_EXTERNAL_URL')
MINIO_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY')
MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_KEY')
MINIO_BUCKET_NAME = os.getenv('MINIO_BUCKET_NAME')

conn = duckdb.connect(database='lab.db')

conn.execute("INSTALL 'ducklake'")
conn.execute("LOAD 'ducklake'")

# Configure S3/MinIO access for DuckLake
conn.execute(f"""
    SET s3_endpoint='{MINIO_EXTERNAL_URL}';
    SET s3_access_key_id='{MINIO_ACCESS_KEY}';
    SET s3_secret_access_key='{MINIO_SECRET_KEY}';
    SET s3_region='us-east-1';
    SET s3_url_style='path';
    SET s3_use_ssl=FALSE;
""")

catalog_path = "lab.ducklake"

# Attach MinIO bucket as a DuckLake catalog
conn.execute(f"""
    ATTACH 'ducklake:{catalog_path}' AS minio_lake (DATA_PATH 's3://{MINIO_BUCKET_NAME}/');
""")
# conn.execute("USE minio_lake")

minio_client = Minio(
    MINIO_EXTERNAL_URL,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)

csv_files = [
    obj.object_name for obj in minio_client.list_objects(MINIO_BUCKET_NAME)
    if obj.object_name.endswith('.csv')
]

for csv_file in csv_files:
    table_name = os.path.splitext(os.path.basename(csv_file))[0]
    s3_path = f"s3://{MINIO_BUCKET_NAME}/{csv_file}"
    try:
        conn.execute(f"CREATE TABLE IF NOT EXISTS {table_name} AS SELECT * FROM '{s3_path}'")
        print(f"Created table: {table_name}")
    except Exception as e:
        print(f"Error creating table {table_name} from {s3_path}: {e}")

# List all schemas
# print("Schemas:", conn.execute("PRAGMA database_list").fetchall())


print("Tables in main:", conn.execute("SHOW TABLES").fetchall())

conn.close()