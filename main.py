from django.db.models import Q
from api.models import User, Agent, Event, Group
from datetime import datetime, timedelta


def get_active_users() -> User:
    today = datetime.today()
    active_users_query = User.objects.filter(
        last_login__gte=(today - timedelta(10)))
    return active_users_query


def get_amount_users() -> User:
    all_users = User.objects.all()
    return all_users.count()


def get_admin_users() -> User:
    all_admins = User.objects.filter(group__name='admin')
    return all_admins


def get_all_debug_events() -> Event:
    debug_events = Event.objects.filter(level='debug')
    return debug_events


def get_all_critical_events_by_user(agent) -> Event:
    critial_events = Event.objects.filter(
        Q(level='critical') & Q(agent=agent))
    return critial_events


def get_all_agents_by_user(username) -> Agent:
    """Traga todos os agentes de associados a um usuário pelo nome do usuário"""
    agents_by_user = Agent.objects.filter(user__name=username)
    return agents_by_user


def get_all_events_by_group() -> Group:
    """Traga todos os grupos que contenham alguem que possua um agente que possuem eventos do tipo information"""
    group_with_information_events = Group.objects.filter(
        user__agent__event__level='information')
    return group_with_information_events
