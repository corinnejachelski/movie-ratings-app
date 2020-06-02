"""CRUD operations"""

from model import db, User, Movie, Rating, connect_to_db
from datetime import datetime

def create_user(email, password):
    """Create and return a new user"""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user 


def get_all_users():
    """Return all Movie objects"""

    return User.query.all()


def get_user_by_id(user_id):

    user = User.query.get(user_id)

    return user


def get_user_by_email(email):

    return User.query.filter_by(email = email).first()


def get_user_id_by_email(email):

    return db.session.query(User.user_id).filter_by(email=email).first()
    

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie"""

    movie = Movie(title=title, overview=overview, release_date=release_date,
                  poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie


def get_all_movies():
    """Return all Movie objects"""

    return Movie.query.all()


def get_movie_by_id(movie_id):

    movie = Movie.query.get(movie_id)

    return movie


def create_rating(user, movie, score):
    """Create and return a new rating"""

    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating


if __name__ == '__main__':
    from server import app
    connect_to_db(app)