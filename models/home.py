from google.appengine.ext import db

#each user has 
class FocusData(db.Model): #TODO is there an easy way to experiment with models in GAE like in Django?
    user = db.UserProperty()
    #session is start and stop time

