from django.contrib import admin
from .models import testOrder, testOrderType

admin.site.register(testOrder)
admin.site.register(testOrderType)