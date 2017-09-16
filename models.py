from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.Unicode(100))
    units = db.Column(db.String(10))
    workouts = db.relationship('Workout', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.name)

class Workout(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    date = db.Column(db.DATETIME)
    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id'))
    notes = db.Column(db.TEXT)
    bodyweight = db.Column(db.NUMERIC)
    exercises = db.relationship('Exercise', backref='workout', lazy='dynamic')

    def __repr__(self):
        return '<Workout %r>' % (self.id)

class Exercises(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(50))
    exercise = db.relationship('Exercise', backref='exercise', lazy='dynamic')

    def __repr__(self):
        return '<Exercises %r>' % (self.name)

class Exercise(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    workout_id = db.Column(db.INTEGER, db.ForeignKey('workout.id'), primary_key=True)
    order = db.Column(db.INTEGER, primary_key=True)
    exercise_id = db.Column(db.INTEGER, db.ForeignKey('exercises.id'))
    sets = db.relationship('Set', backref='exercise', lazy='dynamic')

    def __repr__(self):
        return '<Exercise %r>' % (self.id)

class Set(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    order = db.Column(db.INTEGER, primary_key=True)
    weight = db.Column(db.NUMERIC)
    reps = db.Column(db.INTEGER)
    exercise_id = db.Column(db.INTEGER, db.ForeignKey('exercise.id'))

    def __repr__(self):
        return '<Set %r>' % (self.id)

# Custom View for db columns
"""
class SetView(ModelView):
    form_columns = ['id', 'order', 'weight', 'reps', 'exercise']
"""