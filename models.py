from __init__ import db

# Models
class Player(db.Model):

class Team(db.Model):

class Game(db.Model):

# Many to Many relationship table
teams = db.Table('teams',
)

players = db.Table('players',

)


