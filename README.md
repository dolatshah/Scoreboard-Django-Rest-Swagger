## Create sqlite database and tables
python manage.py migrate

## Run the server
python manage.py runserver

## Access Rest framework UI
localhost:8000

## Access the documentation 
localhost:8000/docs/


## Run taste cases in scoreboard/tests.py
python manage.py test

## Access admin dashboard 

localhost:8000/admin

## Get players list

/players/

## Create a new player

Post /players/

{
    "name": "test",
    "address": "test",
    "points": 0,
    "age": 1
}


## Get a specific player information

GET /players/<pk>


## Delete a player

Delete /players/<pk>


## Update score of a player
/pointsUpdate/<pk>/

{
    "action" : "plus"
}

or 

{
    "action" : "minus"
}
