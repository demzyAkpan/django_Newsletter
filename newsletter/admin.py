from django.contrib import admin
from . models import Newletter, Subscriber

# Register your models here.
admin.site.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email')


admin.site.register(Newletter)
class Newsletter(admin.ModelAdmin):
    list_display = ('title')
    search_fields = ('title', 'body')