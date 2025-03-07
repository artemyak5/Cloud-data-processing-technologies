import boto3

bucket_name = "my-aws-bucket-for-labs"

files_to_upload = [
    ("D:\\programming\\2024-2025\\Cloud-data-processing-technologies\\Lab2\\News_Category_Dataset_v3.json", "data/News_Category_Dataset_v3.json"),
    ("D:\\programming\\2024-2025\\Cloud-data-processing-technologies\\Lab2\\Zomato-data-.csv", "data/Zomato-data-.csv"),
]

s3 = boto3.client('s3')

for local_file, s3_key in files_to_upload:
    try:
        s3.upload_file(local_file, bucket_name, s3_key)
        print(f"Файл {local_file} успішно завантажено в {bucket_name}/{s3_key}")
    except Exception as e:
        print(f"Помилка при завантаженні {local_file}: {e}")

