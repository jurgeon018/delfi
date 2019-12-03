from django.contrib import admin 
from core.models import *
from .admin import *


class ManagerAdmin(admin.AdminSite):
    site_title = 'Delfibus site'
    index_title = 'Delfibus'
    site_header= 'Delfibus Admin'

manager_admin_site = ManagerAdmin(name='manager_admin_site')

manager_admin_site.register(Direction)
manager_admin_site.register(Time)
manager_admin_site.register(Stop)
manager_admin_site.register(Seat)
manager_admin_site.register(SeatInOrder, SeatInOrderAdmin)
manager_admin_site.register(Race, RaceAdmin)

manager_admin_site.register(Index)
manager_admin_site.register(About)
manager_admin_site.register(Park)
manager_admin_site.register(Blog)
manager_admin_site.register(Service)

manager_admin_site.register(BusComment)
manager_admin_site.register(BusGood)
manager_admin_site.register(Bus)
manager_admin_site.register(Post, PostAdmin)

manager_admin_site.register(Order)
manager_admin_site.register(Payment)
manager_admin_site.register(Contact)
manager_admin_site.register(EuropeContact)
manager_admin_site.register(BusContact)


# admin.site.register(Direction)
# admin.site.register(Time)
# admin.site.register(Stop)
# admin.site.register(Seat)
# admin.site.register(SeatInOrder, SeatInOrderAdmin)
# admin.site.register(Race, RaceAdmin)

# admin.site.register(Index)
# admin.site.register(About)
# admin.site.register(Park)
# admin.site.register(Blog)
# admin.site.register(Service)

# admin.site.register(BusComment)
# admin.site.register(BusGood)
# admin.site.register(Bus)
# admin.site.register(Post, PostAdmin)

# admin.site.register(Order)
# admin.site.register(Payment)
# admin.site.register(Contact)
# admin.site.register(EuropeContact)
# admin.site.register(BusContact)