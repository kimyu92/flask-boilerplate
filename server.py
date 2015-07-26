import os
from app import app #from app directory import app obj

# run the whole app
if __name__ == "__main__":
  app.secret_key = os.urandom(12)
  app.run(debug=True, host='0.0.0.0', port=5000)

