import os

"""
https://github.com/mitsuhiko/flask/wiki/Large-app-how-to

1. _basedir is a trick for you to get the folder where the script runs
2. DEBUG indicates that it is a dev environment, you'll get the very helpful error page from flask when an error occurs.
3. SECRET_KEY will be used to sign cookies. Change it and all your users will have to login again.
4. ADMINS will be used if you need to email information to the site administrators.
5. SQLALCHEMY_DATABASE_URI and DATABASE_CONNECT_OPTIONS are SQLAlchemy connection options (hard to guess)
6. THREADS_PER_PAGE my understanding was 2/core... might be wrong :)
7. CSRF_ENABLED and CSRF_SESSION_KEY are protecting against form post fraud
8. RECAPTCHA_* WTForms comes with a RecaptchaField ready to use... just need to go to recaptcha website and get your public and private key.

"""

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

ADMINS = frozenset(['kimyu_92@hotmail.com'])
SECRET_KEY = ''

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://kimyu92:123456@127.0.0.1:3306/flask_demo_db'
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = "somethingimpossibletoguess"

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
RECAPTCHA_OPTIONS = {'theme': 'white'}

