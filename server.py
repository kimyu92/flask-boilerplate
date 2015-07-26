from flask_wtf.csrf import CsrfProtect
from app import app #from app directory import app obj

# To enable CSRF protection for all your view handlers, 
# you need to enable the CsrfProtect module:
csrf = CsrfProtect()

# run the whole app
if __name__ == "__main__":
  csrf.init_app(app)
  app.run(debug=True, host='0.0.0.0', port=5000)
