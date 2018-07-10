# Angular 6 and Python Flask Skeleton

[![Build Status](https://travis-ci.org/tiagoReichert/angular6-flask-skeleton.svg?branch=master)](https://travis-ci.org/tiagoReichert/angular6-flask-skeleton)

This is a base project that can be used to create your applications using Angular 6 (created using Angular-CLI) and Python Flask built with separated Docker containers.

## Testing the Stack
#### Requirements:
- Docker (https://docs.docker.com/install/linux/docker-ce/centos/)
- Docker Compose (https://docs.docker.com/compose/install/#install-compose)

To test this stack you can use the following docker-compose configuration:
```yaml
version: '3'

services:
  frontend:
    restart: always
    image: tiagoreichert/angular6-flask-skeleton_frontend
    ports:
      - "80:80"
    depends_on:
      - 'backend'
  backend:
    restart: always
    image: tiagoreichert/angular6-flask-skeleton_backend
    command: 'python main.py runserver'
    depends_on:
      - 'postgres'
  postgres:
    restart: always
    image: postgres:9.6
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=postgres
    volumes:
      - postgresql:/var/lib/postgresql
volumes:
  postgresql:
    driver: local
```

Step by step to run sample stack:

```console
# Create the docker-compose.yml file
curl -o docker-compose.yml https://raw.githubusercontent.com/tiagoReichert/angular6-flask-skeleton/master/docker-compose-demo.yml

# Start the stack
docker-compose -p skeleton up

# From another terminal window create the database schema and sample entries
docker exec -it skeleton_backend_1 python main.py createdb
```

Now you should be able to open the aplication with [`http://localhost`](http://localhost)
 on your browser.


## Using this skeleton as base development project:
The idea of this project is to be used as base for your own project,
for that do following steps:

```console
# Clone this git repository without commit history
git clone --depth 1 https://github.com/tiagoReichert/angular6-flask-skeleton.git

# Access the Project folder
cd angular6-flask-skeleton

# ... Do the changes on the project as desired...

# Build and start the stack locally
docker-compose up --build

# Creating the Database Schema and adding Demo Users (change on file 'backend/main.py')
docker exec -it angular6-flask-skeleton_backend_1 python main.py createdb
```


