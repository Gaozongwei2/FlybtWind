from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Flybtwind'

app.config.from_object("app.config")
