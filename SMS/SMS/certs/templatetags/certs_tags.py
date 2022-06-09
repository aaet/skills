from django import template

from certs.models import Users

register = template.Library()


@register.simple_tag()
def get_users():
    return Users.objects.all()


@register.inclusion_tag('certs/list_users.html')
def show_users():
    users = Users.objects.all()
    return {"users": users}
