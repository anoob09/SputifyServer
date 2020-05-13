from src.server import db

class Users(db.Model):
    userId = db.Column(db.String(30), primary_key=True)
    token = db.Column(db.String(255), unique = True, nullable = False)
    refreshToken = db.Column(db.String(255), unique = True, nullable = False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def add(self):
        try:
            db.session.add(self)
        except Exception as e:
            print('not inserted')
        db.session.commit()
