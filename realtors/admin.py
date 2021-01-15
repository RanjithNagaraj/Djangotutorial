from django.contrib import admin

# Register your models here.

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name','is_mvp')

admin.site.register(Realtor,RealtorAdmin)