from django.contrib import admin
from durgaapi_with_restframework_APP.models import Employee


#___________________________________________________________________________________________________________________
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'eno', 'ename', 'esal', 'eaddr']

admin.site.register(Employee, EmployeeAdmin)








