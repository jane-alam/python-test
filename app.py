import os
from app import create_app

app = create_app('blueprints')

if __name__ == '__main__':
   app.run(debug=True, use_reloader=True)