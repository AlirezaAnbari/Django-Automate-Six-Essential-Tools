from django.contrib import admin

from .models import (
    Student,
    Customer,
    Employee,
)

class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'roll_no', 'name', 'age',
    ]
    
    
admin.site.register(Student, StudentAdmin)
admin.site.register(Customer)
admin.site.register(Employee)
