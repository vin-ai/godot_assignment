from django.core.cache import cache
from rest_framework import viewsets

from .models import Member, Partner
from .serializers import MemberSerializer, PartnerSerializer


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all().order_by('-on_created')
    serializer_class = PartnerSerializer


class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer

    def get_queryset(self):
        return Member.objects.filter(partner=self.kwargs['partner_pk']) \
            .order_by('-on_created')
