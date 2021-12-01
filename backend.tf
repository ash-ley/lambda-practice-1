terraform {
  backend "s3" {
    bucket         = "talent-academy-439272626435-tfstate-ashley"
    key            = "sprint2/lambda-practice-1/terraform.tfstates"
    dynamodb_table = "terraform-lock"
  }
}