# Flask boilerplate

## Author: Kim Yu Ng

## Instruction:

1. install python3, recommended thru brew install for mac osx user
1. optional: brew install pyvenv
1. optional: pyvenv uh-env (since I placed uh-env is in .gitignore)
1. optional: source uh-env/bin/activate
1. pip3 install -r requirements.txt
1. setup database by making alias on .bashrc or .bash_profile (refer below)
1. python3 server.py
1. enjoy

## Dependency:

* Flask framework == 0.10.1
* Jinja2 == 2.7.3 
* SQLAlchemy == 1.0.8
* Flask-SQLAlchemy == 2.0
* PyMySQL == 0.6.6 //pure python MySQL connector
* ...


## Setup database

* open .bashrc or .bash_profile
* export UH_DB_USER="WhateverMySQLUsername"
* export UH_DB_PASSWORD="WhateverMySQLPassword"
* export UH_DB_ADDRESS="WhateverServerAddress"
* create db user thru MySQL user 
```sql
* mysql -u root -p -h hostaddress
* CREATE USER 'USERNAME'@'hostname' IDENTIFIED BY 'MYPASSWORD';
* CREATE DATABASE database name;
* GRANT ALL ON database name.* TO 'kimyu92'@'hostname';
```
* tips: replace 'hostname' with '%' for remote server access
* populate models.py thru shell


## Populate all models.py to database

* python shell.py
* from app import db
* db.create_all()
* exit()


## Overview Structure

    ├── .bowerrc  
    ├── .gitignore  
    ├── bower.json  
    ├── package.json  
    ├── app  
    │   ├── app.py  
    │   │   ├── static  
    │   │   ├── bower_components  
    │   │   ├── css  
    │   │   │   └── style.css  
    │   │   ├── scripts  
    │   │   ├── templates  
    │   │   │   └── users  
    │   │   │        ├── login.html  
    │   │   │        └── register.html  
    │   │   ├── hello.html  
    │   │   └── index.html  
    ├── requirements.txt  
    ├── config.py  
    ├── server.py  
    └── shell.py  


## Frontend Guide for Bower + React + Gulp
1. node (recommend to use nvm install v0.12 -> nvm use v0.12)
1. node -v => # 0.12
1. npm install -g bower
1. npm install -g gulp
1. npm install
1. bower install
1. gulp clean && gulp
* to add more dependency eg. jquery: bower install package-name --save


## Reference:
* https://github.com/mitsuhiko/flask/wiki/Large-app-how-to
* https://realpython.com/blog/python/the-ultimate-flask-front-end/
* https://realpython.com/blog/python/the-ultimate-flask-front-end-part-2/

## Feel free to fork it! :)
