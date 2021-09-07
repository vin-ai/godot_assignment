# urls.py
from django.urls import path, include
from rest_framework_nested import routers
from partners.viewsets import PartnerViewSet, MemberViewSet

router = routers.SimpleRouter()
router.register('partners', PartnerViewSet)

partners_router = routers.NestedSimpleRouter(router, 'partners', lookup='partner')
partners_router.register('members', MemberViewSet, basename='partner-members')
# 'basename' is optional. Needed only if the same viewset is registered more than once
# Official DRF docs on this option: http://www.django-rest-framework.org/api-guide/routers/

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('', include(partners_router.urls)),
]
