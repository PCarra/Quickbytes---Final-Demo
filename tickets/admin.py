'''
  // written by: Patrick Carra
  // tested by: Patrick Carra
  // debugged by: Patrick Carra
  // etc.
'''

from django.contrib import admin
from . models import Orderstable, Itemtable, Alertstable

# Register your models here.
admin.site.register(Orderstable)
admin.site.register(Itemtable)
admin.site.register(Alertstable)
