from flask import Flask
from flask_migrate import Migrate
import models
from routes import book_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = "fXaSXNS-L5eYP9_3e-ctVQFZclnGOSj9"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///./database/book.db'

models.init_app(app)
app.register_blueprint(book_blueprint)

migrate = Migrate(app, models.db)

if __name__ == '__main__':
    app.run(debug=False, port=5002, host="0.0.0.0")
