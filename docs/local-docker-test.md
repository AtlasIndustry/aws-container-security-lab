# Local Docker Test

## Objective

Validate that the sample Flask application can be built and run as a Docker container before deploying it to AWS.

## Steps Completed

- Created a basic Flask application with health, login, and admin routes.
- Created a Dockerfile using the Python 3.11 slim base image.
- Built the Docker image locally.
- Ran the container on port 5000.
- Tested browser access to `/`, `/health`, and `/admin`.
- Tested failed and successful login attempts with PowerShell.
- Confirmed that security-relevant application logs are generated.

## Security-Relevant Events

The app currently generates logs for:

- Login attempts
- Failed logins
- Successful logins
- Admin endpoint access attempts

These logs will later be forwarded to AWS CloudWatch and used for detection engineering scenarios.

## Observed HTTP Responses

- `GET /` returned `200 OK`
- `GET /health` returned `200 OK`
- `GET /admin` returned `200 OK`
- `POST /login` with invalid credentials returned `401 Unauthorized`
- `POST /login` with valid credentials returned `200 OK`
- `GET /login` returned `405 Method Not Allowed` because the route only accepts POST requests

## Next Step

Push the first working version to GitHub, then prepare the app for AWS deployment.