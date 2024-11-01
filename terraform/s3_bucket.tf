module "s3_bucket" {
  source = "terraform-aws-modules/s3-bucket/aws"

  bucket = "nasa_data_bucket"
  acl    = "private"

  control_object_ownership = true
  object_ownership         = "ObjectWriter"

  versioning = {
    enabled = true
  }
}

output "bucket_name" {
  value = aws_s3_bucket.nasa_data_bucket.id
}