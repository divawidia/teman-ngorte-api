from app import app
from controller import UserController

@app.route('/')
def index():
    return 'Hello'

@app.route('/register', methods=['POST'])
def users():
    return UserController.register()

@app.route('/login', methods=['POST'])
def logins():
    return UserController.login()
