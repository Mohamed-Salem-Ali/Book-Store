"""
WSGI config for Book_store project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""
import sys
import os

# Add your project directory to the sys.path
sys.path.insert(0, '/home/MohamedSalemAli/book_library /Book_store')

# Activate your virtual environment
activate_this = '/home/MohamedSalemAli/.virtualenvs/venv/bin/activate_this.py'
exec(open(activate_this).read(), {'__file__': activate_this})

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'Book_store.settings'

# Import Django's WSGI handler and set it as the application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
