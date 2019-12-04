import os
from decouple import config

DEFAULT_FROM_EMAIL = 'Delfibus Site Team'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# https://myaccount.google.com/lesssecureapps
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
print(EMAIL_HOST_PASSWORD, EMAIL_HOST_USER)
# /etc/profile



