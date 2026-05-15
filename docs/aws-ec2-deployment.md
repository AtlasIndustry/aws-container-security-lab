# AWS EC2 Deployment

## Objective

Deploy the Dockerized Flask security lab application to an AWS EC2 instance and validate that the containerized workload can run in a cloud environment.

## AWS Environment

- Cloud Provider: AWS
- Compute Service: EC2
- Operating System: Ubuntu Server
- Container Runtime: Docker
- Application Port: 5000
- Deployment Method: GitHub clone and local Docker build on EC2

## Deployment Steps Completed

- Launched an Ubuntu EC2 instance.
- Configured inbound security group access for SSH and application testing.
- Connected to the instance over SSH.
- Installed Docker on the EC2 instance.
- Enabled Docker to start on boot.
- Added the `ubuntu` user to the Docker group.
- Installed Git.
- Cloned the GitHub repository onto the EC2 instance.
- Built the Docker image on the EC2 instance.
- Ran the container on port 5000.
- Validated browser access to the application using the EC2 public IPv4 address.

## Security Group Configuration

Temporary testing access was configured for:

- TCP 22 for SSH access from my IP address.
- TCP 5000 for application testing from my IP address.

Port 5000 was used for initial lab validation only. This is not a production-ready exposure pattern.

## Security Notes

The current deployment proves that the containerized workload can run on AWS, but it is not hardened yet.

Current limitations:

- The Flask development server is still being used.
- The app is exposed directly on port 5000.
- There is not yet centralized logging in CloudWatch.
- There is not yet a reverse proxy or TLS configuration.
- The container is not yet configured with stronger runtime restrictions.
- The deployment is manual and not yet managed through infrastructure-as-code.

## Next Step

Harden the deployment by improving network exposure, adding CloudWatch logging, and documenting risks before moving toward Terraform-based infrastructure deployment.