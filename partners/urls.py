from django.urls import path

from .views import add_partner, add_member

app_name = 'partners'

urlpatterns = [
    path('', add_partner, name='add'),
    path('member', add_member, name='member-add'),
]
