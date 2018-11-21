"""
WSGI config for gemuesekoop project.

It exposes the WSGI callable as a module-level variable named ``application``.

"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gemuesekoop.settings")

application = get_wsgi_application()

