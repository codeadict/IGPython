"""
WSGI config for igpython project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.
"""
import os
import site
from datetime import datetime

# Remember when mod_wsgi loaded the app to monitor it with Nagios
wsgi_loaded = datetime.now()


# Tell WSGI where to look for settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# Add the project base dir to the python path so we can import manage.
wsgidir = os.path.dirname(__file__)
site.addsitedir(os.path.abspath(os.path.join(wsgidir, '../')))

# manage adds /apps, /lib, and /vendor to the Python path.
import manage

import django.conf
import django.core.handlers.wsgi
import django.core.management
import django.utils

# Do validate and activate translations like using `./manage.py runserver`.
# http://blog.dscpl.com.au/2010/03/improved-wsgi-script-for-use-with.html
utility = django.core.management.ManagementUtility()
command = utility.fetch_command('runserver')
command.validate()

# This is what mod_wsgi runs.
django_app = django.core.handlers.wsgi.WSGIHandler()

def application(env, start_response):
    env['wsgi.loaded'] = wsgi_loaded
    env['datetime'] = str(datetime.now())
    return django_app(env, start_response)

# Uncomment this to figure out what's going on with the mod_wsgi environment.
# def application(env, start_response):
#     start_response('200 OK', [('Content-Type', 'text/plain')])
#     return '\n'.join('%r: %r' % item for item in sorted(env.items()))