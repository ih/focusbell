from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from models.home import FocusData

#TODO move this to a separate file
def debug():
    import sys
    import pdb
    pdb.Pdb(stdin=getattr(sys,'__stdin__'),stdout=getattr(sys,'__stderr__')).set_trace(sys._getframe().f_back)


class HomePage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
#        pdb.set_trace()  TODO add pdb support via the debug function http://opensourcehacker.com/2011/02/28/debugging-app-engine-application-with-python-pdb-debugger/
        if user: #TODO ensure every user has a focus_data object when they are created
            focus_data = get_focus_data_for(user) 
            template_values = {'focus_data': focus_data}
            debug()
            self.response.out.write(template.render('templates/home.html', template_values)) 
        else:
            self.redirect(users.create_login_url(self.request.uri))

#TODO currently a stub, implement true functionality
#TODO move this a location that improves code organization
#return FocusData object for the given user
def get_focus_data_for(user):
    focus_data = FocusData()
    focus_data.user = user
    return focus_data

    #FocusData.gql("WHERE author = :1", user=user) 

