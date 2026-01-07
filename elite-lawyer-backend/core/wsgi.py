"""
WSGI entrypoint for Vercel deployment
"""

import os
import sys

# Add the backend root to Python path so 'core' can be found
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# If your project is inside 'core/', add it too
sys.path.append(os.path.join(current_dir, "core"))

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

from django.core.wsgi import get_wsgi_application

# WSGI application
application = get_wsgi_application()

# Vercel serverless handler
app = application
