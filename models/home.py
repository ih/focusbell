from google.appengine.ext import db
from google.appengine.api import users
from library.app_engine import debug
from settings import MINIMAL_INTERVAL
#records time between user pressing start and stop
#TODO change this to models.py file in the root directory since there aren't many models

class FocusSession(db.Model):
    user = db.UserProperty(auto_current_user_add=True) #TODO create a db.Model user then make this a ReferenceProperty, makes accessing user objects more sensible
    start = db.DateTimeProperty(auto_now_add=True)
    stop = db.DateTimeProperty()

    def length(self):
        return self.stop - self.start

    
class Alert(db.Model):
    time = db.DateTimeProperty(auto_now_add=True)
    was_focused = db.BooleanProperty()
    session = db.ReferenceProperty(FocusSession)
    interval = db.IntegerProperty()

    @staticmethod
    def last_interval(user):
        last_session = FocusSession.all().filter('user = ', user).order('-start')
        user_alerts = last_session.get().alert_set
        if user_alerts != None and user_alerts.count() > 0:
            return user_alerts.order('-time').get()
        else:
            return MINIMAL_INTERVAL


    
