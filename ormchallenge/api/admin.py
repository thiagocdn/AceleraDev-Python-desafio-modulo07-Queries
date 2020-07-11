from django.contrib import admin

# Register your models here.
from api.models import Agent, Event, Group, User


class AgentModeEvent(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'env', 'version', 'address')


class EventModeEvent(admin.ModelAdmin):
    list_display = ('id', 'level', 'data', 'arquivado',
                    'date', 'agent_id')


class GroupModeEvent(admin.ModelAdmin):
    list_display = ('id', 'name')


class UserModeEvent(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_login', 'email', 'password')


admin.site.register(Agent, AgentModeEvent)
admin.site.register(Event, EventModeEvent)
admin.site.register(Group, GroupModeEvent)
admin.site.register(User, UserModeEvent)
