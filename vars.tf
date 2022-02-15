variable AWS_REGION {
    type = string
    default = "us-east-1"
    description = "Région de notre instance ec2"
}

variable AWS_AMIS {
  type = map
  default = {
    "us-east-1" = "ami-038b3df3312ddf25d"
  }
}