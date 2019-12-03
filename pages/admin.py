from django.contrib import admin 
from pages.models import * 
from core.admin.admin_site import manager_admin_site


manager_admin_site.register(Index)
manager_admin_site.register(About)
manager_admin_site.register(Contact)
manager_admin_site.register(Park)
manager_admin_site.register(Blog)














