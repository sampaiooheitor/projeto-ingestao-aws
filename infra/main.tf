provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "datalake" {
  bucket = "projeto-ingestao-heitor"

  versioning {
    enabled = true
  }

  lifecycle {
    prevent_destroy = false
  }
}

resource "aws_glue_catalog_database" "catalog" {
  name = "projeto_dados_db"
}
