import sae
import os
import sys

root = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(root, 'site-packages'))
#sys.path.insert(0, os.path.join(root, 'site-packages.zip'))
import django

#def app(environ, start_response):
#    status = '200 OK'
#    response_headers = [('Content-type', 'text/plain')]
#    start_response(status, response_headers)
#    return [django.get_version()]

#print django.get_version()

#application = sae.create_wsgi_app(app)

from lookupip import wsgi
application = sae.create_wsgi_app(wsgi.application)

