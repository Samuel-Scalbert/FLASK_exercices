from .app import app,db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(45))
    user_firstname = db.Column(db.String(45))
    user_surname = db.Column(db.String(45))
    user_surname = db.Column(db.Text)
    user_password_hash = db.Column(db.Text)
    user_birthyear = db.Column(db.DateTime)
    user_promotion_date = db.Column(db.String(45))
    user_description = db.Column(db.Text)
    user_last_seen = db.Column(db.DateTime)
    user_linkedin = db.Column(db.Text)
    user_github = db.Column(db.Text)
    user_inscription_time = db.Column(db.DateTime)

class Post(db.Model):
    
class followers(db.Model):
    
class CV(db.Model):
    
class Comment(db.Model):
    
class Message(db.Model):
    
class skills(db.Model):
    
class competences(db.Model):