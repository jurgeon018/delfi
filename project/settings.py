import os
from decouple import config
from django.utils.translation import ugettext_lazy as _
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURRENT_DOMEN = config('CURRENT_DOMEN') or 'http://127.0.0.1:8000'
SECRET_KEY = config('SECRET_KEY') or 'ss'
DEBUG = True
print(DEBUG)
print(CURRENT_DOMEN)
print(SECRET_KEY)
ADMINS = (
  ('Andrew', 'jurgeon018@gmail.com'), 
  # ('', ''),
)
ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'project.wsgi.application'
LANGUAGE_CODE = 'ru-ru'
# LANGUAGE_CODE = 'en-us' 
TIME_ZONE = 'Europe/Kiev'
# TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
# USE_TZ = True
LANGUAGES = (
  ('ru', _('Russian')),
  # ('en', _('English')),
  ('uk', _('Ukrainian')),
)
LOCALE_PATHS = (
  os.path.join(BASE_DIR, 'locale'),
)
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
SITE_ID=1
LOGIN_URL = "/admin/"
ROSETTA_MESSAGES_PER_PAGE = 100
AUTOTRANSLATE_TRANSLATOR_SERVICE = 'autotranslate.services.GoSlateTranslatorService'
# AUTOTRANSLATE_TRANSLATOR_SERVICE = 'autotranslate.services.GoogleAPITranslatorService'
# GOOGLE_TRANSLATE_KEY="6f5fe2dd463dc0620c3b1b4262eb28977214f773"
DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.sqlite3',
      'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
  }
}

from .TINYMCE import *
from .EMAIL import *
from .INSTALLED_APPS import *
from .MIDDLEWARE import *
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': 'delfibus_db',
        # 'USER' : 'jurgeon018',
        # 'PASSWORD' : '69018',
        # 'HOST' : '127.0.0.1',
        # 'PORT' : '5432',
    }
}

LIQPAY_PUBLIC_KEY = "sandbox_i29048427621"
LIQPAY_PRIVATE_KEY = "sandbox_RBR5FM04gXXt25MLzVmP7eyarKDWIKXw86MEMkvm"

# LIQPAY_PUBLIC_KEY = "i3466565002"
# LIQPAY_PRIVATE_KEY="85pd0UjyxXThv8RQpmPld4Z406wGZF4huAfqDHaB"










# REDIS_HOST = 'localhost'
# REDIS_PORT = '6379'
# BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
# BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600} 
# CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'

# CELERY_TIMEZONE = 'Asia/Makassar'
CELERY_BROKER_URL = 'amqp://127.0.0.1//'
# CELERY_BROKER_URL = 'redis://127.0.0.1:6379//'
# CELERY_ACCEPT_CONTENT = ['json']
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_BEAT_SCHEDULE = {
    # 'third-task':{
    #     'task':'app1.tasks.task_three',
    #     'schedule': 2.0,
    #     # 'args': 
    # },
    # 'fourth-task':{
    #     'task':'app1.tasks.task_four',
    #     'schedule': 3.0,
    #     # 'args': 
    # },
    # 'fifth-task':{
    #     'task':'app1.tasks.task_five',
    #     'schedule': crontab(minute=59, hour=23),
    #     # 'schedule': crontab(minute=0, hour='*/3,10-19'),
    #     # 'schedule': crontab(hour=16, day_of_week=5),
    #     # 'schedule': 3600.0,
    #     # 'schedule': solar('sunset', -37.81753, 144.96715),
    # },
    # 'sixth-task':{
    #     'task':'core.tasks.create_races_every_night',
    #     'schedule':3.0
    # }

}

