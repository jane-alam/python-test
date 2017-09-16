from app import app
from models import Users

@app.route('/')
def homepage():
    return "Hello World"