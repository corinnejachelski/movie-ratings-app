"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!
@app.route('/')
def display_homepage():
    """View homepage"""

    return render_template('homepage.html')

@app.route('/login')
def login():

    email = request.args.get('login_email')
    password = request.args.get('login_password')

    user = crud.get_user_by_email(email)
    

    if user:
        if user.password == password:
            session['user_id'] = crud.get_user_id_by_email(email)
            print(session)
            flash("Logged in! Hello, " + email)
            return redirect("/")
    else:
        flash("A user with that email and password does not exist")
        return redirect("/")


@app.route('/users', methods=["POST"])
def create_new_user():

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email) 
    if user:
        flash("Account with that email already exists. Please try again.")
    else: 
        crud.create_user(email, password)
        flash("User account successfully created. Please log in.")

    return redirect('/')

@app.route('/users')
def show_all_users():
    """Show a list of all users"""

    users = crud.get_all_users()

    return render_template('all_users.html', users=users)

@app.route('/user/<user_id>')
def show_user(user_id):

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)

@app.route('/movies')
def show_all_movies():
    """Show a list of all movies"""

    movies = crud.get_all_movies()

    return render_template('all_movies.html', movies=movies)


@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """Show detals on a particular movie"""

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
