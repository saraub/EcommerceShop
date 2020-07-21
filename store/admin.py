from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderedItem)
admin.site.register(ShippingAddress)
admin.site.register(Category)


