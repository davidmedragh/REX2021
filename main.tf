provider "aws" {
    region = "${var.AWS_REGION}"
    access_key ="XXXXXXXXXXXXXXXXXXXXXXX"
    secret_key ="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
}
resource "aws_instance" "my_ec2_instance" {
    ami             = "${var.AWS_AMIS[var.AWS_REGION]}"
    instance_type   = "t2.micro"
}
