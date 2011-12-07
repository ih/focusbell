from settings import *
from google.appengine.ext.webapp import template
import os

#from http://opensourcehacker.com/2011/02/28/debugging-app-engine-application-with-python-pdb-debugger/
def debug():
    import sys
    import pdb
    pdb.Pdb(stdin=getattr(sys,'__stdin__'),stdout=getattr(sys,'__stderr__')).set_trace(sys._getframe().f_back)


def render(handler, template_path, context): #TODO move this to a different location (utilities file?)
    path = os.path.join(ROOT, TEMPLATES_ROOT+template_path)
    return handler.response.out.write(template.render(path, context))
