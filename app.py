from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

admin = Admin(app)


from views import *

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Workout, db.session))
admin.add_view(ModelView(Exercises, db.session))
admin.add_view(ModelView(Exercise, db.session))
admin.add_view(ModelView(Set, db.session))


if __name__ == '__main__':
    app.run()