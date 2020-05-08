# Anaconda

## Environtment Variables
```
POSTGRES_URL (default: postgres_db <- docker container)
POSTGRES_DB (default: anaconda_db)
POSTGRES_USER (default: user)
POSTGRES_PASS (default: pass)
```

## Installation
Flask installation can be read [here](https://flask.palletsprojects.com/en/1.1.x/installation)

## Running application

### Docker Compose
- make sure [docker](https://docs.docker.com/) and [docker compose](https://docs.docker.com/compose/) is already installed
- make sure the [docker network](https://docs.docker.com/network/) is configured well (or just create "docker_local" network for default)
- navigate to the application's directory
- run ```docker-compose up --build``` in the application directory

### Python virtual env
- python version used : 3.6
- navigate to the application's directory
- run ```pip install -r requirements.txt```
- run ```python app.py```
- run ```flask db init && \ flask db migrate && \ flask db upgrade```
    
##Endpoints
-  /item [GET]
-  /item [POST]
    
    body example 
    ```
    {
        "name": "new item"
   }
   ```
- /item/[id] [GET]
- /item/[id] [PATCH]
    
    body example 
    ```
    {
        "name": "new item"
   }
   ```
- /item/[id] [DELETE]