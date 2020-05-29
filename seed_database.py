"""Automate populating database"""

import os
import json
from random import choice, randint
from datetime import datetime
import crud, model, server 

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()


with open('data/movies.json') as file:
    movie_data = json.loads(file.read())

#Create movies, store them in list for 
#creating  fake user ratings later

movies_in_db = []

for movie in movie_data:
    title, overview, poster_path = (movie['title'], 
                                    movie['overview'],
                                    movie['poster_path'])
    release_date = datetime.strptime(movie['release_date'], "%Y-%m-%d")

    db_movie = crud.create_movie(title, overview, release_date, poster_path)

    movies_in_db.append(db_movie)

    #Create users

for n in range(10):
    email = f"user{n}@test.com"
    password = "test"

    user = crud.create_user(email, password)

    for i in range(10):
        random_movie = choice(movies_in_db)
        score = randint(1, 5)

        crud.create_rating(user, random_movie, score)
