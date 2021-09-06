from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page

from .models import Member, Partner
from .serializers import MemberSerializer, PartnerSerializer


class PartnerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Partner.objects.all().order_by('-on_created')
    serializer_class = PartnerSerializer

    # @method_decorator(cache_page(60 * 60))
    # @action(detail=False, methods=['get'], name='List Partner Members', basename='members')
    # def featured(self, request):
    #     members = Member.objects.all().order_by('-on_created')
    #     serializer = MemberSerializer(members, many=True)

    #     res = Response(serializer.data)
    #     res['Cache-Control'] = 'max-age: 300'
    #     return res


class MemberViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Member.objects.all().order_by('-on_created')
    serializer_class = MemberSerializer
