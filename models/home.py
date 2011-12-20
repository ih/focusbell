from google.appengine.ext import db
from google.appengine.api import users
#records time between user pressing start and stop
class FocusSession(db.Model):
    user = db.UserProperty(auto_current_user_add=True)
    start = db.DateTimeProperty(auto_now_add=True)
    stop = db.DateTimeProperty()
    
class Alert(db.Model):
    time = db.DateTimeProperty(auto_now_add=True)
    was_focused = db.BooleanProperty()
    session = db.ReferenceProperty(FocusSession)
    interval = db.IntegerProperty()
    
