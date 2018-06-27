# Angular 6 and Python Flask Skeleton

This is an base project that can be used to create your applications using Angular 6 (created using Angular-CLI) and Python Flask built with separated docker containers.


##### Starting the Stack:
```
# Build and start the Stack
docker-compose up --build

# Creating the Database Schema and adding Demo Users (change on file 'backend/main.py')
docker exec -it angular6-flask-skeleton_backend_1 python main.py createdb
```