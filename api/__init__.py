from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://saleor:saleor@localhost:5432/testdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.Date)
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))
        }

# with app.app_context():
#     db.create_all()
#     from datetime import datetime
#     current_date = datetime.today().date()
#     new_post = Post(title="A new morning", description="A new morning details", created_at=current_date)

#     db.session.add(new_post)
#     db.session.commit()


@app.route('/')
def hello():
    return 'My First API !!'