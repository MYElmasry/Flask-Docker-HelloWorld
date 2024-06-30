# Flask Docker HelloWorld


This repository contains a Dockerized Flask application that serves a couple of simple endpoints.

## Files Included

- **Dockerfile**: Specifies the Docker image configuration. It pulls the latest Python image, installs Flask from `requirements.txt`, and runs `hello.py` on port 5000.
  
- **requirements.txt**: Lists the Python packages required for the application. Currently, it includes only Flask.

- **hello.py**: The main Flask application file. It defines two routes:
  - `/`: Displays a simple "Hello, World!" message.
  - `/mo`: Displays a customized "Hello, World from mo!" message in red text.

## Usage

### Building the Docker Image

To build the Docker image, navigate to the directory containing `Dockerfile` and run:

```bash
docker build -t flask-docker-app .
```
### Running the Docker Container

Once the image is built, you can run the Docker container with

```bash
docker run -d -p 5000:5000 flask-docker-app
```
