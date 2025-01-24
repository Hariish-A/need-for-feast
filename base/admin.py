from django.contrib import admin
from .models import Items, Order, User,Restaurant,Customer,Owner,Deliverer

# Register your models here.
admin.site.register(Items)
admin.site.register(Order)
admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Owner)
admin.site.register(Deliverer)

