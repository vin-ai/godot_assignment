from django.urls import path

from .views import add_partner, add_member

app_name = 'partners'

urlpatterns = [
    path('', add_partner, name='add'),
    path('<int:pk>/', add_partner, name='update'),
    path('<int:pk>/member/', add_member, name='member-add'),
    path('<int:pk>/member/<int:mem_pk>/', add_member, name='member-update'),
]
