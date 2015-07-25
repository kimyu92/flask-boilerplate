from __init__ import db

class Player(db.Model):
  '''
  Information about player
  Information includes name, picture, position, player number, weight etc.
  '''

  name = db.Column(db.String(256), primary_key=True)
  picture = db.Column(db.String(256), unique=True)
  experience_years = db.Column(db.String(256))
  draft_info = db.Column(db.String(256))
  position = db.Column(db.String(256))
  player_number = db.Column(db.String(256))
  current_team = db.Column(db.String(256))
  college = db.Column(db.String(256))
  birth_info = db.Column(db.String(256))
  weight = db.Column(db.String(256))
  twitter = db.Column(db.String(256))
  age = db.Column(db.String(256))
  youtube_link_1 = db.Column(db.String(256))
  youtube_link_2 = db.Column(db.String(256))
  youtube_link_3 = db.Column(db.String(256))
  career_GS = db.Column(db.String(256))
  career_REB = db.Column(db.String(256))
  career_BLK = db.Column(db.String(256))
  career_FT_PCT = db.Column(db.String(256))
  career_DR = db.Column(db.String(256))
  career_MIN = db.Column(db.String(256))
  career_FG_PCT = db.Column(db.String(256))
  career_3PM_A = db.Column(db.String(256))
  career_OR = db.Column(db.String(256))
  career_FGM_A = db.Column(db.String(256))
  career_STL = db.Column(db.String(256))
  career_TO = db.Column(db.String(256))
  career_3PM_PCT = db.Column(db.String(256))
  career_AST = db.Column(db.String(256))
  career_GP = db.Column(db.String(256))
  career_PF = db.Column(db.String(256))
  career_PTS = db.Column(db.String(256))
  CAREER_FTM_A = db.Column(db.String(256))
  season_TO = db.Column(db.String(256))
  season_GS = db.Column(db.String(256))
  season_FG_PCT = db.Column(db.String(256))
  seasonseason__PTS = db.Column(db.String(256))
  season_OR = db.Column(db.String(256))
  season_GP = db.Column(db.String(256))
  season_PF = db.Column(db.String(256))
  season_REB = db.Column(db.String(256))
  season_FTM_A = db.Column(db.String(256))
  season_BLK = db.Column(db.String(256))
  season_MIN = db.Column(db.String(256))
  season_STL = db.Column(db.String(256))
  season_AST = db.Column(db.String(256))
  season_FT_PCT = db.Column(db.String(256))
  season_FGM_A = db.Column(db.String(256))
  season_3P_PCT = db.Column(db.String(256))
  season_DR = db.Column(db.String(256))
  season_3PM_A = db.Column(db.String(256))
  team_name = db.Column(db.String(256), db.ForeignKey('team.name'))


class Team(db.Model):
  '''
  Information about Team 
  Information includes name, conference, division, site_name, city, state, mascot
  '''

  players = db. relationship('Player', backref='team', lazy='dynamic')
  name = db.Column(db.String(256), primary_key=True)
  conference = db.Column(db.String(256))
  division = db.Column(db.String(256))
  site_name = db.Column(db.String(256))
  city = db.Column(db.String(256))
  state = db.Column(db.String(256))
  mascot = db.Column(db.String(256))

teams = db.Table('teams',
  db.Column('team_name', db.String(256), db.ForeignKey('team.name')),
  db.Column('game_id', db.Integer, db.ForeignKey('game.id'))
)

players = db.Table('players',
  db.Column('player_name', db.String(256), db.ForeignKey('player.name')),
  db.Column('game_id', db.Integer, db.ForeignKey('game.id'))
)

class Game(db.Model):
  '''
  Information about Game
  Information include home_team, away_team, data, home_score, away_score, etc.
  '''

  id = db.Column(db.Integer, primary_key=True)
  home_team = db.Column(db.String(256))
  away_team = db.Column(db.String(256))
  date = db.Column(db.String(256))
  home_score = db.Column(db.String(256))
  away_score = db.Column(db.String(256))
  home_box_fgm = db.Column(db.String(256))
  home_box_fga = db.Column(db.String(256))
  home_box_fg3m = db.Column(db.String(256))
  home_box_fg3a = db.Column(db.String(256))
  home_box_ftm = db.Column(db.String(256))
  home_box_fta = db.Column(db.String(256))
  home_box_oreb = db.Column(db.String(256))
  home_box_dreb = db.Column(db.String(256))
  home_box_ast = db.Column(db.String(256))
  home_box_stl = db.Column(db.String(256))
  home_box_blk = db.Column(db.String(256))
  home_box_to = db.Column(db.String(256))
  home_box_pf = db.Column(db.String(256))
  home_box_pts = db.Column(db.String(256))
  home_box_plus_minus = db.Column(db.String(256))
  away_box_fgm = db.Column(db.String(256))
  away_box_fga = db.Column(db.String(256))
  away_box_fg3m = db.Column(db.String(256))
  away_box_fg3a = db.Column(db.String(256))
  away_box_ftm = db.Column(db.String(256))
  away_box_fta = db.Column(db.String(256))
  away_box_oreb = db.Column(db.String(256))
  away_box_dreb = db.Column(db.String(256))
  away_box_ast = db.Column(db.String(256))
  away_box_stl = db.Column(db.String(256))
  away_box_blk = db.Column(db.String(256))
  away_box_to = db.Column(db.String(256))
  away_box_pf = db.Column(db.String(256))
  away_box_pts = db.Column(db.String(256))
  away_box_plus_minus = db.Column(db.String(256))

  #many to many team game relationship
  teams = db.relationship('Team', secondary=teams,
    backref=db.backref('games', lazy='dynamic'))

  #many to many player game relationship
  players = db.relationship('Player', secondary=players,
    backref=db.backref('games', lazy='dynamic'))
