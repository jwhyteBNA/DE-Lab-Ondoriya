import os
import io
import time
from logger import get_logger
import requests
from minio import Minio
from dotenv import load_dotenv

load_dotenv()

logger = get_logger("ingestion.log")

MINIO_EXTERNAL_URL = os.getenv('MINIO_EXTERNAL_URL')
MINIO_BUCKET_NAME = os.getenv('MINIO_BUCKET_NAME')
minio_client = Minio(
    MINIO_EXTERNAL_URL,
    access_key=os.getenv('MINIO_ACCESS_KEY'),
    secret_key=os.getenv('MINIO_SECRET_KEY'),
    secure=False
)

BASE_URL = os.getenv('BASE_URL')

FILES_TO_INGEST = [
    "faction_distribution.csv",
    "households.csv",
    "language_building_blocks.csv",
    "language_roots.csv",
    "moons.csv",
    "people.csv",
    "planets.csv",
    "region_biome.csv",
    "regions.csv"
]

def get_files_to_ingest(FILES_TO_INGEST):
    file_urls = [f"{BASE_URL}{file_name}" for file_name in FILES_TO_INGEST]
    return file_urls


def ingest_files_to_minio(file_urls):
    for file_url in file_urls:
        start_time=time.time()
        response = requests.get(file_url)
        if response.status_code == 200:
            file_name = file_url.split("/")[-1]
            minio_client.put_object(
                MINIO_BUCKET_NAME,
                file_name,
                io.BytesIO(response.content),
                len(response.content)
            )
            duration = time.time() - start_time
            logger.info(f"Successfully ingested {file_name} from {file_url} in {duration:.2f} seconds")
        else:
            logger.error(f"Failed to retrieve {file_url} (status code: {response.status_code})")


def main():
    file_urls = get_files_to_ingest(FILES_TO_INGEST)
    ingest_files_to_minio(file_urls)

if __name__ == "__main__":
    main()
