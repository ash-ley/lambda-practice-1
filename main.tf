resource "aws_iam_role" "lambda_role" {
  name = "lambda_role"

  assume_role_policy = <<EOF
{
      "Version" : "2012-10-17",
      "Statement" : [
          {
            "Action" : [
                "sts:AssumeRole"
            ],
            "Principal" : {
                "Service" : "lambda.amazonaws.com"
            },
            "Effect" : "Allow",
            "Sid" : "LambdaRole"
          }
      ]
}
EOF
}

resource "aws_iam_policy" "my_policy" {
  name = "my-role"
   description = "My policy"

  policy = <<-EOF
  {
        "Version" : "2012-10-17",
        "Statement" : [
          {
            "Action" : [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*",
            "Effect" : "Allow",
            "Sid" : "cloudwatchLambda"
          },
          {
            "Action" : [
                "s3:*"
            ],
            "Effect" : "Allow",
            "Sid" : "S3ObjectActions",
            "Resource" : ["arn:aws:s3:::talent-academy-439272626435-tfstate-ashley"]
            }
      ]
  }
EOF
}

resource "aws_iam_role_policy_attachment" "test-attach" {
  role       = "${aws_iam_role.lambda_role.name}"
  policy_arn = "${aws_iam_policy.my_policy.arn}"
}