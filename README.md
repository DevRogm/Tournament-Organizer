# Tournament-Organizer

## General information
Tournament Organizer is a web application for quickly creating and managing tree tournaments. 
The application allows you to choose 2, 4, 8, 16 or 32 players. 
After adding all players and starting the tournament, 
the application generates a tree and draws pairs for the first round. 
Entering the results and confirming them causes the winner of a given game to automatically 
advance to the next round. Finally, once the tournament winner is determined, the tournament is automatically ended.


## Technologies
* Python
* Django
* Django Rest Framework

## Back End
The application was built using the Django framework, and the Django Rest Framework library was used to develop endpoints.

### Installation and running
After cloning the repository, you need to create and activate a virtual environment and install the necessary 
dependencies in it:

    $ python -m venv venv

    $ source venv/bin/activate/

    $ pip install -r requirements.txt

The application should be launched from the manage.py file with the command:

    $ python manage.py runserver


You can test the application locally:

    http://127.0.0.1:8000/

Available endpoints:
* api/tournaments/ - list of all tournaments created by the organizer - [GET, POST]
    * Example GET response:

          [
              {
                  "id": 11,
                  "name": "Tekken 7",
                  "num_of_players": 4,
                  "description": "The first tekken 7 tournament",
                  "organizer": {
                      "username": "admin",
                      "email": "admin@admin.pl"
                  },
                  "tournament_status": "complete",
                  "players": [
                      {
                          "id": 53,
                          "name": "Mario"
                      },
                      {
                          "id": 54,
                          "name": "Luigi"
                      },
                      {
                          "id": 55,
                          "name": "Luna"
                      },
                      {
                          "id": 56,
                          "name": "Lila"
                      }
                  ]
              }
          ]     

* api/tournaments/{id} - details of the tournament with the given id - [GET, PUT, PATCH, DELETE]
* api/players/ - list of all players created by the organizer - [GET, POST]
     * Example GET response:

            [
                {
                    "id": 56,
                    "name": "Lila"
                },
                {
                    "id": 54,
                    "name": "Luigi"
                },
                {
                    "id": 55,
                    "name": "Luna"
                },
                {
                    "id": 53,
                    "name": "Mario"
                }
            ]

* api/players/{id} - details of the player with the given id - [GET, PUT, PATCH, DELETE]
  * Example GET response:
    
        {
            "id": 56,
            "name": "Lila"
        }
    
* api/games/ - list of generated matches after the tournament starts - [GET, POST]
  * Example GET response:

        [
          {
              "id": 32,
              "name": "Tekken_7_game_1_1",
              "player_1": {
                  "id": 55,
                  "name": "Luna"
              },
              "player_2": {
                  "id": 54,
                  "name": "Luigi"
              },
              "score_1": null,
              "score_2": null,
              "is_approved": false,
              "game_round": 1,
              "game_num": 1
          },
          {
              "id": 33,
              "name": "Tekken_7_game_1_2",
              "player_1": {
                  "id": 53,
                  "name": "Mario"
              },
              "player_2": {
                  "id": 56,
                  "name": "Lila"
              },
              "score_1": null,
              "score_2": null,
              "is_approved": false,
              "game_round": 1,
              "game_num": 2
          },
          {
              "id": 34,
              "name": "Tekken_7_game_2_1",
              "player_1": null,
              "player_2": null,
              "score_1": null,
              "score_2": null,
              "is_approved": false,
              "game_round": 2,
              "game_num": 1
          }
        ]


* api/games/{id} - details of the match at the given id - [GET, PUT, PATCH, DELETE]
* api/auth/login - endpoint for user login - [POST]
  * Example POST request: 

        {
            "username": "admin",
            "password": "admin"
        }  

  * Example response: 

        {
           "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMTcyNjU3NCwiaWF0IjoxNzExNjQwMTc0LCJqdGkiOiIyOGQ3MDQ5NmQ5YTE0NDdjYTE4NjA5YWYyMDQ4ODJmNyIsInVzZXJfaWQiOjF9.kb4JHWY13_ikvNtVXgBws4F258clu8IwJZIwiMgi4tc",
          "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MjMyMTc0LCJpYXQiOjE3MTE2NDAxNzQsImp0aSI6ImQxYTg4YTY1NGEzMDRiZDc5MmZjNjBjNDcxMWQ2Y2JjIiwidXNlcl9pZCI6MX0.tEM7Qb9VwvIfMyD0P7v0hyzu-C_na3KgNXKBtKCn4eE",
          "id": 1,
          "username": "admin",
          "email": "admin@admin.pl",
          "is_admin": true,
          "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MjMyMTc0LCJpYXQiOjE3MTE2NDAxNzQsImp0aSI6ImE1ODFjMzNjMjgzMTQxN2Y4ZDM0YjAwNWE0MzE3YTU2IiwidXNlcl9pZCI6MX0.PBKuJFnWv65l-EWfXQ1oNABG0320-Ap21RYlG6PPxq8"
        } 


* api/auth/user - information about the logged organizer - [GET]
  * Example GET response:
    
         {
             "id": 1,
             "username": "admin",
             "email": "admin@admin.pl",
             "is_admin": true
         }  


* api/schema/docs/ - documentation generated by Swagger

## Front End
The application does not yet have a developed front-end, but the graphic design concept is presented below
so that you can imagine how such an application will look and work.

### Creating a new tournament
To create a 'pending' tournament, simply provide its name, number of players and optionally a description.

![](github_img/1_create.png )
<p align="left">
    pic.1 Create new tournament
</p>

### Main application view
In the main application view we have buttons such as:
* login/logout
* profile
* homepage
* create a tournament
* tournaments not started
* ongoing tournaments
* tournaments ended

![](github_img/2_main_view.png )
<p align="left">
    pic.2 Main view
</p>

### Pending tournaments
Below you can see an example of tournaments that have not started.
You can enter such a tournament, edit it and start it.

![](github_img/3_pending_tournaments.png)
<p align="left">
    pic.3 Pending tournaments list
</p>

### Pending tournament view
In this example situation, players must be added before the tournament can begin.


![](github_img/4_pending_tournament_view.png)
<p align="left">
    pic.4 Pending tournament view
</p>

### List of added players
Adding players to the tournament allows it to start. After clicking the button
'Start tournament' tree is generated as below.

![](github_img/5_player_names.png)
<p align="left">
    pic.5 Added players
</p>

![](github_img/6_tree.png)
<p align="left">
    pic.6 Tournament tree view
</p>

## What's next...???
The application will be expanded to include player statistics.
When creating a tournament, you will be able to choose whether the tournament concerns any sport.
If so, "matches" could be generated, e.g. for football,
and the details of such a match will be typical for the given sport.
Add docker to run applications more easily.


