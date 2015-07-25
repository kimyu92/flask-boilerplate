from __init__ import db
import models

# create db schema based on model
db.create_all()
print('Database schema created\n')