import os
from decouple import config

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# https://myaccount.google.com/lesssecureapps
# EMAIL_HOST_USER = "jurgeon018@gmail.com"
# EMAIL_HOST_PASSWORD = "yfpfhrj69001"
EMAIL_HOST_USER = "delfibus@starwayua.com"
EMAIL_HOST_PASSWORD = "starway69018"

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

DEFAULT_RECIPIENTS = [
    'jurgeon018@gmail.com',
    'delfibus0068@gmail.com',
],