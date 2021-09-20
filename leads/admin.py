from django.contrib import admin
from .models import User, Leads, Agent, UserProfile

# Register your models here.
admin.site.register(Leads)
admin.site.register(UserProfile)
admin.site.register(User)
admin.site.register(Agent)
