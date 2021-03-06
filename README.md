## Install the required packages
```bash

pip install -r requirements.txt
```

## Create sqlite database and tables
```bash

python manage.py migrate
```
## Run the server
```bash
python manage.py runserver
```
## Access Rest framework UI
[localhost:8000](http://localhost:8000)

## Access the documentation 
[localhost:8000/docs](http://localhost:8000/docs/)


## Run test cases in scoreboard/tests.py
```bash
python manage.py test
```
## Access admin dashboard 

[localhost:8000/admin](http://localhost:8000/admin)

## Get players list
```bash
GET /players/
```

## Create a new player
```bash
POST /players/

data = {
    "name": "test",
    "address": "test",
    "points": 0,
    "age": 1
}
```

## Get a specific player information
```bash
GET /players/<pk>
```

## Delete a player
```bash
DELETE /players/<pk>
```

## Update score of a player
```bash
POST /pointsUpdate/<pk>/

data = {
    "action" : "plus"
}

or 

data = {
    "action" : "minus"
}
```