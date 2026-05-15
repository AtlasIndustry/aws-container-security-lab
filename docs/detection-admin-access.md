# Detection: Admin Endpoint Access

## Objective

Create a basic CloudWatch detection for access to the Flask application's `/admin` endpoint.

## Detection Source

- Application: Dockerized Flask application
- Host: Ubuntu EC2 instance
- Log file: `/home/ubuntu/aws-container-security-lab/logs/app.log`
- CloudWatch log group: `/aws/ec2/aws-container-security-lab/app`

## Detection Pattern

The application generates the following log event when the admin endpoint is accessed:

```text
[ADMIN_ACCESS_ATTEMPT] ip=<client_public_ip> user_agent=<browser_user_agent>