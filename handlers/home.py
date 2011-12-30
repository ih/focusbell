from google.appengine.api import users
from google.appengine.ext import webapp
from models.home import FocusSession, Alert
from library.app_engine import debug, render
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
        #use the last interval from the previous session as the first interval in the current session
        initial_interval = Session.last_interval()
        #create a new session
        session = FocusSession()
        key = session.put() 
        template_values = {'session_key': key, 'interval': initial_interval} #TODO add interval from previous session and use to initilize current interval
        render(self, 'stop.html', template_values)

    @staticmethod
    def last_interval():#TODO make last_interval a static method of Alert
        return Alert.all().order('-time').get().interval 

class StopSession(webapp.RequestHandler):
    def post(self):
        session = FocusSession.get(self.request.get('key'))
        session.stop = datetime.datetime.now()
        session.put()
        #TODO get all past sessions and display in summary
        times = StopSession.session_lengths()

        #TODO send alert data to be displayed
        template_values = {'session_length': session.stop - session.start, 'sessions': times, 'alerts': Alert.all().order('-time')}
        render(self, 'summary.html', template_values)

    @staticmethod
    def session_lengths():
        times = [session.stop - session.start for session in FocusSession.all().order('-start') if session.stop]
        return times
            

class SaveAlert(webapp.RequestHandler):
    def post(self):
        #todo it'd be nice to process the request data as json
        #debug()
        was_focused = False
        if self.request.get('was_focused') == 'true':
            was_focused = True
        session = FocusSession.get(self.request.get('session'))
        interval = int(self.request.get('interval'))
        alert = Alert(was_focused=was_focused, session=session, interval=interval)
        alert.put()
        

