from airflow.models import Variable
import json
# Should be using Airflow Variable to get these Global Vars.
# Which are already been setup in the docker-compose.yaml file
# ex: AWS_S3_BUCKET = Variable.get("AWS_S3_BUCKET")
# https://cloud.google.com/storage/docs/samples/storage-transfer-manager-upload-directory#storage_transfer_manager_upload_directory-python
GCP_CREDENTIALS_FILE_PATH = Variable.get("GCP_CREDENTIALS_FILE_PATH")
GCP_PROJECT_ID = Variable.get('GCP_PROJECT_ID')
BUCKET_NAME = Variable.get('BUCKET_NAME')
BUCKET_CLASS = Variable.get('BUCKET_CLASS')
BUCKET_LOCATION = Variable.get('BUCKET_LOCATION')
DATASET_NAME = Variable.get('DATASET_NAME')
DBT_ACCOUNT_ID = Variable.get('DBT_ACCOUNT_ID')
DBT_CONN_ID = Variable.get('DBT_CONN_ID')

# 從 Airflow Variable 中獲取 JSON 字串並解析成 Python 字典
dbt_jobs_id_str = Variable.get('DBT_JOBS_ID')
DBT_JOBS_ID = json.loads(dbt_jobs_id_str)