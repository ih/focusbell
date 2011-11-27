from google.appengine.api import users
from google.appengine.ext import webapp

class HomePage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.out.write('Welcome to FocusBell %s!' % user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))
