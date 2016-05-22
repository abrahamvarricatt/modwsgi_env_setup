


# import os
# import sys
# from django.core.wsgi import get_wsgi_application
#
# sys.path.append('/srv/sources/bottle')
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
#
# application = get_wsgi_application()


import pip


def application(environ, start_response):
    status = '200 OK'

    installed_packages = pip.get_installed_distributions()
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
         for i in installed_packages])

    output = '\n'.join(map(str, installed_packages_list))

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return output


