from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template


class HomePage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            template_values = {}
            self.response.out.write(template.render('templates/home.html', template_values)) #TODO implement template_path
        else:
            self.redirect(users.create_login_url(self.request.uri))
