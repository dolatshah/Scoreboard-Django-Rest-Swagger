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


## Run taste cases in scoreboard/tests.py
```bash
python manage.py test
```
## Access admin dashboard 

[localhost:8000/admin](http://localhost:8000/admin)

## Get players list
```bash
/players/
```

## Create a new player
```bash
Post /players/

{
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
Delete /players/<pk>
```

## Update score of a player
/pointsUpdate/<pk>/

{
    "action" : "plus"
}

or 

{
    "action" : "minus"
}
