from google.appengine.api import users
from google.appengine.ext import webapp
from models.home import FocusData
from library.app_engine import debug, render
class HomePage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user: #TODO ensure every user has a focus_data object when they are created
            focus_data = get_focus_data_for(user) 
            template_values = {'focus_data': focus_data}

            render(self, 'home.html', template_values)
        else:
            self.redirect(users.create_login_url(self.request.uri))

#TODO currently a stub, implement true functionality
#TODO move this a location that improves code organization
#return FocusData object for the given user
def get_focus_data_for(user):
    focus_data = FocusData()
    focus_data.user = user
    return focus_data



