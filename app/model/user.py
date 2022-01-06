from app import db
from datetime import datetime, date
from alembic import op

class User(db.Model):
    user = db.Table('user',
      db.Column('id', db.BigInteger, primary_key=True, autoincrement=True),
      db.Column('name', db.String(250), nullable=False),
      db.Column('email', db.String(60), index=True, unique=True, nullable=False),
      db.Column('password', db.String(250), nullable=False),
      db.Column('created_at', db.DateTime, default=datetime.utcnow),
      db.Column('updated_at', db.DateTime, default=datetime.utcnow)
    )

    
    # op.bulk_insert(user, [{
    #   'id':1, 'name':'John Smith', 'email': 'john@gmail.com', 'password': '123345','created_at':date(2010, 10, 5), 'updated_at':date(2010, 10, 5)
    #   }]
    # )
  
    def __repr__(self):
        return '<User {}>'.format(self.name)