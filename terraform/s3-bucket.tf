resource "aws_s3_bucket" "nasa_data_bucket" {
  bucket = "nasa-data-storage-bucket"
}

output "bucket_name" {
  value = aws_s3_bucket.nasa_data_bucket.id
}