'''
  // written by: Patrick Carra
  // tested by: Patrick Carra
  // debugged by: Patrick Carra
  // etc.
'''

from django.contrib import admin
from . models import SupplyOrder, Ingredients

# Register your models here.
admin.site.register(SupplyOrder)
admin.site.register(Ingredients)
