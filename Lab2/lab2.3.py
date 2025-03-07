import boto3
import os
from dotenv import load_dotenv

# Завантаження змінних середовища
load_dotenv()

# Отримуємо значення з .env
bucket_name = os.getenv("AWS_BUCKET_NAME")
file_key = os.getenv("S3_FILE_KEY")
local_file_path = os.getenv("LOCAL_FILE_PATH")

s3 = boto3.client('s3')

# Завантаження файлу з S3
s3.download_file(bucket_name, file_key, local_file_path)

# Читання вмісту файлу
with open(local_file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("=== Перші 5 рядків файлу ===")
for line in lines[:5]:
    print(line.strip())  
