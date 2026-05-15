# CloudWatch Logging

## Objective

Configure centralized logging for the AWS-hosted containerized Flask application using the Amazon CloudWatch Agent.

## Logging Architecture

The application runs inside a Docker container on an Ubuntu EC2 instance.

The container logs are written to a host-based log file:

```bash
/home/ubuntu/aws-container-security-lab/logs/app.log