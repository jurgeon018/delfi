from django.contrib import admin 
from core.models import *
from .admin import *


class ManagerAdmin(admin.AdminSite):
    site_title = 'Delfibus site'
    index_title = 'Delfibus'
    site_header= 'Delfibus Admin'

manager_admin_site = ManagerAdmin(name='manager_admin_site')

# core 
manager_admin_site.register(Direction, DirectionAdmin)
manager_admin_site.register(Time, TimeAdmin)
manager_admin_site.register(Stop, StopAdmin)
manager_admin_site.register(Seat, SeatAdmin)
manager_admin_site.register(SeatInOrder, SeatInOrderAdmin)
manager_admin_site.register(Race, RaceAdmin)

# pages 
manager_admin_site.register(Index, IndexAdmin)
manager_admin_site.register(About, AboutAdmin)
manager_admin_site.register(Park, ParkAdmin)
manager_admin_site.register(Blog, BlogAdmin)
manager_admin_site.register(Service, ServiceAdmin)

# content
manager_admin_site.register(Bus, BusAdmin)
manager_admin_site.register(BusGood, BusGoodAdmin)
manager_admin_site.register(BusComment, BusCommentAdmin)
manager_admin_site.register(Post, PostAdmin)


# order 
manager_admin_site.register(Order, OrderAdmin)
manager_admin_site.register(Payment, PaymentAdmin)
manager_admin_site.register(Contact, ContactAdmin)
manager_admin_site.register(EuropeContact, EuropeContactAdmin)
# manager_admin_site.register(BusContact, BusContactAdmin)



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