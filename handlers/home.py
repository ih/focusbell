from google.appengine.api import users
from google.appengine.ext import webapp
from models.home import FocusSession, Alert
from library.app_engine import debug, render
from settings import MINIMAL_INTERVAL
#import json
import datetime

class HomePage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user: 
            template_values = {'user': user}
            render(self, 'home.html', template_values)
        else:
            self.redirect(users.create_login_url(self.request.uri))

class Session(webapp.RequestHandler):
    def post(self):
        user = users.get_current_user()
        #use the last interval from the previous session as the first interval in the current session
        if user:
            #create a new session
            session = FocusSession()
            key = session.put() 
            initial_interval = Alert.last_interval(user)
            template_values = {'session_key': key, 'interval': initial_interval} 
            render(self, 'stop.html', template_values)
        else:
            self.redirect(users.create_login_url(self.request.uri))

class StopSession(webapp.RequestHandler):
    def post(self):
        user = users.get_current_user()
        if user:
            session = FocusSession.get(self.request.get('key'))
            session.stop = datetime.datetime.now()
            session.put()
            user_sessions = FocusSession.all().filter('user = ', user).order('-start')
            sessions = []
            for user_session in user_sessions:
                user_session.intervals = [alert.interval for alert in user_session.alert_set if user_session.alert_set.count() > 0]
                sessions.append(user_session)
            
            #TODO send alert data to be displayed, make sure alerts are for a user and pair with each session
            template_values = {'session_length': session.stop - session.start, 'sessions': sessions, 'logout_url': users.create_logout_url(self.request.uri)}
            render(self, 'summary.html', template_values)
        else:
            self.redirect(users.create_login_url(self.request.uri))

class SaveAlert(webapp.RequestHandler):
    def post(self):
        #todo it'd be nice to process the request data as json
        was_focused = False
        if self.request.get('was_focused') == 'true':
            was_focused = True
        session = FocusSession.get(self.request.get('session'))
        interval = int(self.request.get('interval'))
        alert = Alert(was_focused=was_focused, session=session, interval=interval)
        alert.put()
        

