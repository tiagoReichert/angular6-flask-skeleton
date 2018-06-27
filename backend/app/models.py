from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Version(db.Model):

    __tablename__ = 'version'

    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.String, nullable=True)
    latest = db.Column(db.Boolean, nullable=False)


class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
           'id': self.id,
           'name': self.name,
           'email': self.email
        }
