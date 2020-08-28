from flask import Flask, jsonify

app = Flask(__name__)
app.config.from_object('config')

from .routes import routes
if __name__ == '__main__':
    app.run()