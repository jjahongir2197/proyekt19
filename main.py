import uuid
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///session_token.db'
db = SQLAlchemy(app)

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer)

    token = db.Column(
        db.String(200),
        unique=True
    )

def create_session(user_id):
    token = str(uuid.uuid4())

    session = Session(
        user_id=user_id,
        token=token
    )

    db.session.add(session)
    db.session.commit()

    return token

with app.app_context():
    db.create_all()

    print(create_session(1))
