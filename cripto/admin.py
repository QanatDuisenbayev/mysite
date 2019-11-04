from django.contrib import admin
from cripto.models import message,UserAccount



class CriptoAdmin(admin.ModelAdmin):

	prepopulated_fields = {'slug': ('title',)}

admin.site.register(message, CriptoAdmin)
admin.site.register(UserAccount)
# Register your models here.
