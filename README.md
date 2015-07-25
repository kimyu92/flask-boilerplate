# Flask boilerplate

## Author: Kim Yu Ng

## Instruction:

1. install python3, recommended thru brew install for mac osx user
1. optional: brew install pyvenv
1. optional: pyvenv name-env
1. optional: source name-env/bin/activate
1. pip3 install -r requirements.txt
1. setup models and populate data (refer below)
1. python3 __init__.py
1. enjoy

## Dependency:

* Flask framework == 0.10.1
* Jinja2 == 2.7.3 
* SQLAlchemy == 1.0.8
* Flask-SQLAlchemy == 2.0
* PyMySQL == 0.6.6 //pure python MySQL connector

## Modification Models.py
* define models aka classes and relationships among them
* under utils/ there is a ddl which helps to create a new schema
* modify the db connector, schema name on config.py
* refer models.sample.py thanks to @lazercorn

## Setup models
* refer modification Models.py 
* run createDB.py

## Feel free to fork it! :)
