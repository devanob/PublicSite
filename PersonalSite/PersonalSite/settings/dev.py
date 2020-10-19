from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qq4v0$-v&eu*9ahf^6h2urd&h@+r(#6%qf&i%h%1r4ixyurbg8'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


    
WEBPACK_LOADER = {

    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': '', # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}

try:
    from .local import *
except ImportError:
    pass

