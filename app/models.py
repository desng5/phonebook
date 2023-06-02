from app import db
from datetime import datetime



# CREATE TABLE user(
#     id SERIAL PRIMARY KEY,
#     first_name VARCHAR(50) NOT NULL,
# )

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone_num = db.Column(db.Numeric(15), nullable=False)
    address = db.Column(db.String(75), nullable=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    email =  db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

    def __repr__(self):
        return f"<person {self.id}|{self.first_name}{self.last_name}{self.phone_num}{self.address}{self.date_created}>"



