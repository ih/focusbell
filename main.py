from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from handlers.home import HomePage
from handlers.home import Session, StopSession, SaveAlert

application = webapp.WSGIApplication(
    [('/', HomePage),
     ('/start', Session),
     ('/stop', StopSession),
     ('/alert', SaveAlert)],
    debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
