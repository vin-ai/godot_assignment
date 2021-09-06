from django.urls import path, include

from rest_framework.routers import DefaultRouter

from partners.viewsets import PartnerViewSet, MemberViewSet

app_name = 'api'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'partner', PartnerViewSet)
router.register(r'member', MemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

for pattern in router.urls:
  print(pattern)
