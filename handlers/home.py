from google.appengine.api import users
from google.appengine.ext import webapp
from models.home import FocusSession
from library.app_engine import debug, render
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
        session = FocusSession()
        key = session.put() #TODO figure out why session is not saving
#        debug()
        template_values = {'session_key': key}
        render(self, 'stop.html', template_values)

class StopSession(webapp.RequestHandler):
    def post(self):
        #TODO set stop time for session
        session = FocusSession.get(self.request.get('key'))
        session.stop = datetime.datetime.now()
        session.put()
        #TODO get all past sessions and display in summary
        template_values = {'session_length': session.stop - session.start}
        render(self, 'summary.html', template_values)




