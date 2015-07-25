# Flask boilerplate

## Author: Kim Yu Ng

## Instruction:

1. install python3, recommended thru brew install for mac osx user
1. optional: brew install pyvenv
1. optional: pyvenv uh-env (since I placed uh-env is in .gitignore)
1. optional: source uh-env/bin/activate
1. pip3 install -r requirements.txt
1. setup models and populate data (refer below)
1. python3 ____init____.py
1. enjoy

## Dependency:

* Flask framework == 0.10.1
* Jinja2 == 2.7.3 
* SQLAlchemy == 1.0.8
* Flask-SQLAlchemy == 2.0
* PyMySQL == 0.6.6 //pure python MySQL connector
* ...

## Modification Models.py
* define models aka classes and relationships among them
* under utils/ there is a ddl which helps to create a new schema
* modify the db connector, schema name on config.py
* refer models.sample.py thanks to @lazercorn

## Setup models
* refer modification Models.py 
* run createDB.py

## Overview Structure
├── .bowerrc

├── .gitignore

├── bower.json

├── package.json

├── app

│   ├── app.py

│   ├── static

│   │   ├── bower_components

│   │   ├── css

│   │   │   └── style.css

│   │   └── scripts

│   └── templates

│       ├── hello.html

│       └── index.html

├── requirements.txt

└── run.sh


## Frontend
1. node (recommend to use nvm install v0.12 -> nvm use v0.12)
1. node -v => # 0.12
1. npm install -g bower
1. npm install
1. bower install
* to add more dependency bower install package-name --save


## Reference:
* https://github.com/mitsuhiko/flask/wiki/Large-app-how-to
* https://realpython.com/blog/python/the-ultimate-flask-front-end/
* https://realpython.com/blog/python/the-ultimate-flask-front-end-part-2/

## Feel free to fork it! :)
