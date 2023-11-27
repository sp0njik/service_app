from django.contrib import admin

from services.models import Subscriptions, Service, Plan

admin.site.register(Service)
admin.site.register(Plan)
admin.site.register(Subscriptions)