from django.apps import AppConfig

class CoreConfig(AppConfig):
    name = 'core'
    verbose_name = "ядро"



class BlogConfig(AppConfig):
    name = 'pages'
    verbose_name = 'блог-посты'
