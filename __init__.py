from flask import Flask, send_file, render_template
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Load config.py
app.config.from_object('config')

# db object (wrapper for SQLAlchemy)
db = SQLAlchemy(app)

@app.route("/")
def index():
  return render_template('index.html') 

# Setup environment
if __name__ == "__main__":
  # app.debug = True

  # run app
  app.run(host='0.0.0.0', port=5000)

