"""Development settings and globals."""

from .base import *


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = get_env_setting('DEBUG', True)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
TEMPLATE_STRING_IF_INVALID = "INVALID EXPRESSION: %s"
########## END DEBUG CONFIGURATION

########## HOST CONFIGURATION
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = get_env_setting('ALLOWED_HOSTS', [])
########## END HOST CONFIGURATION

########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': root('myproject.db'),
  }
}
########## END DATABASE CONFIGURATION

########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHE_BACKEND = get_env_setting(
    'CACHE_BACKEND', 'django.core.cache.backends.locmem.LocMemCache')

CACHES = {
    'default': {
        'BACKEND': CACHE_BACKEND,
        'LOCATION': get_env_setting('CACHE_DEFAULT', 'cache-default'),
        'OPTIONS': get_env_setting('CACHE_OPTIONS', {})
    }
}

########## END CACHE CONFIGURATION

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION
