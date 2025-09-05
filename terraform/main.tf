resource "aws_instance" "docker_host" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type
  user_data     = file("${path.module}/user_data.sh")
  tags = {
    Name = "docker-host"
  }
}
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"] # Canonical
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}
output "public_ip" {
  value = aws_instance.docker_host.public_ip
}
