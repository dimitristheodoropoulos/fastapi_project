Enterprise FastAPI Project
This is an enterprise-grade FastAPI application with a modular structure, using best practices for scalability and maintainability. This guide will help you set up the project locally with necessary services such as NGINX, PostgreSQL, and MongoDB.

Table of Contents
Project Setup
Service Configuration
NGINX
PostgreSQL
MongoDB
Run the Application
Testing
Additional Notes
Setup
Clone this repository.

git clone https://github.com/your-username/fastapi_project.git
cd fastapi_project


Create a virtual environment and activate it.

python3 -m venv fastenv
source fastenv/bin/activate  # On Windows use: fastenv\Scripts\activate


Install dependencies:

pip install -r requirements.txt

Services
NGINX
NGINX will act as a reverse proxy to serve the FastAPI app in a production environment.

Docker Setup for NGINX
Create a nginx.conf file:

Create a file called nginx.conf in the root of your project folder.

Example nginx.conf:
server {
    listen 80;
    server_name localhost;

    location / {
        proxy_pass http://fastapi_project:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

Dockerize NGINX:

In your docker-compose.yml, you can add an NGINX service that uses this configuration.

Example Docker Compose setup with NGINX:

version: '3'

services:
  fastapi_project:
    build: .
    ports:
      - "8000:8000"
    networks:
      - fastapi_network

  nginx:
    image: nginx:alpine
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    ports:
      - "80:80"
    depends_on:
      - fastapi_project
    networks:
      - fastapi_network

networks:
  fastapi_network:
    driver: bridge

Run NGINX in Docker:

With this configuration, running docker-compose up will start both the FastAPI app and the NGINX reverse proxy.

PostgreSQL (Relational Database)
This FastAPI application can be connected to a PostgreSQL database for structured data.

Docker Setup for PostgreSQL
Add PostgreSQL Service to Docker Compose:

In your docker-compose.yml, add the following PostgreSQL service:
postgres:
  image: postgres:latest
  environment:
    POSTGRES_DB: fastapi_db
    POSTGRES_USER: fastapi_user
    POSTGRES_PASSWORD: password
  ports:
    - "5432:5432"
  volumes:
    - postgres_data:/var/lib/postgresql/data
  networks:
    - fastapi_network


Configure the FastAPI App:

Update your database settings in app/config.py:
DATABASE_URL = "postgresql://fastapi_user:password@postgres/fastapi_db"

Run Database Migrations:

You can run the migrations after the services are up:
docker-compose exec fastapi_project alembic upgrade head


MongoDB (NoSQL Database)
You can also use MongoDB as a NoSQL option for storing unstructured data.

Docker Setup for MongoDB
Add MongoDB Service to Docker Compose:

Add a MongoDB service in your docker-compose.yml:
mongo:
  image: mongo:latest
  ports:
    - "27017:27017"
  networks:
    - fastapi_network


Configure the FastAPI App:

Update the MongoDB connection in app/config.py:
MONGO_URI = "mongodb://mongo:27017/fastapi_db"


Run the Application
Start Services with Docker Compose:

In your project directory, run the following command to start all services (FastAPI, PostgreSQL, MongoDB, and NGINX):
docker-compose up --build

This will start the FastAPI app on port 8000, PostgreSQL on port 5432, MongoDB on port 27017, and NGINX on port 80.

Access the App:

After running the application, you can access it at:

http://localhost:8000 for the FastAPI app (direct access)
http://localhost for the FastAPI app through NGINX (reverse proxy)


Testing
Run the tests with pytest:
docker-compose exec fastapi_project pytest
Make sure all services (NGINX, PostgreSQL, and MongoDB) are running and configured correctly before running the tests.

Additional Notes
NGINX: NGINX is set up as a reverse proxy for the FastAPI app. You can access it directly or through NGINX, depending on your configuration.
PostgreSQL and MongoDB: Both databases are set up as Docker services. The FastAPI app is configured to connect to them using their respective container names.
Docker Compose: Using Docker Compose simplifies service orchestration. The docker-compose.yml file defines all services and ensures they can communicate on the same network.
This documentation should help you run the FastAPI project with Docker, NGINX, PostgreSQL, and MongoDB. Let me know if you need further assistance!

This version of the documentation includes all the steps required to run the project in Docker, with the necessary configurations for PostgreSQL, MongoDB, and NGINX.
