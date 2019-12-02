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
manager_admin_site.register(Order, OrderAdmin)
manager_admin_site.register(Payment, PaymentAdmin)
manager_admin_site.register(Question, QuestionAdmin)
manager_admin_site.register(Post, PostAdmin)
manager_admin_site.register(BusComment, BusCommentAdmin)
manager_admin_site.register(Bus, BusAdmin)
manager_admin_site.register(Page, PageAdmin)


# admin.site.register(Direction)
# admin.site.register(Time)
# admin.site.register(Stop)
# admin.site.register(Seat)
# admin.site.register(SeatInOrder)#, SeatInOrderAdmin)
# admin.site.register(Race, RaceAdmin)
# admin.site.register(Order, OrderAdmin)
# admin.site.register(Payment, PaymentAdmin)
# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Post, PostAdmin)
# admin.site.register(BusComment, BusCommentAdmin)



