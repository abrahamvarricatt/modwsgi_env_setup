


import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/srv/sources/bottle')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

application = get_wsgi_application()


# def application(environ, start_response):
#     status = '200 OK'
#     output = 'Hello World!\n\n'
#
#     response_headers = [('Content-type', 'text/plain'),
#                         ('Content-Length', str(len(output)))]
#     start_response(status, response_headers)
#
#     return [output]


