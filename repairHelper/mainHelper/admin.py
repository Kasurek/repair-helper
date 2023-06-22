from django.contrib import admin
from .models import Repair, Customer, DeviceType, SparePart
# Register your models here.
class RepairAdmin(admin.ModelAdmin):
    readonly_fields = ('startDate', 'lastUpdate')

admin.site.register(Repair,RepairAdmin)
admin.site.register(Customer)
admin.site.register(DeviceType)
admin.site.register(SparePart)