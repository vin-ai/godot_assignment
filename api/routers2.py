from django.urls import path

# from rest_framework.routers import DefaultRouter

from partners.viewsets import PartnerViewSet, MemberViewSet

app_name = 'api'

# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'partner', PartnerViewSet)
# router.register(r'member', MemberViewSet)

partner_list = PartnerViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

partner_detail = PartnerViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    # 'delete': 'destroy'
})

member_list = MemberViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

member_detail = MemberViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    # 'delete': 'destroy'
})

urlpatterns = [
    path('partners/', partner_list, name='partner-list'),
    path('partner/<int:pk>/', partner_detail, name='partner-detail'),
    path('partner/<int:pk>/members/', member_list, name='member-list'),
    path('partner/<int:pk>/member/<int:mem_pk>/',
         member_detail, name='member-detail'),
]

# for pattern in router.urls:
#   print(pattern)
