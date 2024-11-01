import os
import requests
import boto3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize AWS S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)

NASA_API_URL = "https://ssd-api.jpl.nasa.gov/cad.api"
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

def fetch_and_save_data():
    """Fetch data from NASA API and save it to S3."""
    response = requests.get(NASA_API_URL)
    if response.status_code == 200:
        data = response.json()
        s3.put_object(
            Bucket=S3_BUCKET_NAME,
            Key="cad_data.json",
            Body=str(data),
            ContentType='application/json'
        )
        print("Data successfully saved to S3.")
    else:
        print("Failed to fetch data from NASA API.")

@app.route('/fetch-data', methods=['POST'])
def fetch_data_endpoint():
    """Fetch data and save it to S3."""
    fetch_and_save_data()
    return jsonify({"message": "Data fetched and saved to S3"}), 200

@app.route('/get-data', methods=['GET'])
def get_data():
    """Provide endpoint to fetch data from S3."""
    obj = s3.get_object(Bucket=S3_BUCKET_NAME, Key="cad_data.json")
    data = obj['Body'].read().decode('utf-8')
    return jsonify({"data": data}), 200

if __name__ == '__main__':
    # Fetch data on startup (optional)
    fetch_and_save_data()
    app.run(host='0.0.0.0', port=5000)