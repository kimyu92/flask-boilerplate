import os
import sys

from flask import Flask, send_file, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Load config.py
app.config.from_object('config')

# db object (wrapper for SQLAlchemy)
db = SQLAlchemy(app)


########################
# Configure Secret Key #
########################
def install_secret_key(app, filename='secret_key'):
  """Configure the SECRET_KEY from a file
  in the instance directory.

  If the file does not exist, print instructions
  to create it from a shell with a random key,
  then exit.
  """
  filename = os.path.join(app.instance_path, filename)

  try:
    app.config['SECRET_KEY'] = open(filename, 'rb').read()
  except IOError:
    print('Error: No secret key. Create it with:')
    full_path = os.path.dirname(filename)
    if not os.path.isdir(full_path):
      print('mkdir -p {filename}'.format(filename=full_path))
    print('head -c 24 /dev/urandom > {filename}'.format(filename=filename))
    sys.exit(1)

if not app.config['DEBUG']:
  install_secret_key(app)


@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')


@app.route('/hello')
def hello():
  return render_template('hello.html')

@app.errorhandler(404)
def not_found(error):
  return render_template('404.html'), 404


from app.users.views import mod as usersModule
app.register_blueprint(usersModule)



# Later on you'll import the other blueprints the same way:
# from app.comments.views import mod as commentsModule
# from app.posts.views import mod as postsModule
# app.register_blueprint(commentsModule)
# app.register_blueprint(postsModule)

# Setup environment
# def app(environ, start_response):
#   data = "Hello, World!\n"
#   start_response("200 OK", [
#       ("Content-Type", "text/plain"),
#       ("Content-Length", str(len(data))) 
#     ])
#   return iter([data])