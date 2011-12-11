from google.appengine.api import users
from google.appengine.ext import webapp
from models.home import FocusSession
from library.app_engine import debug, render
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

    def put(self):
        #TODO set stop time for session
        return None



