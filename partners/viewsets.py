from rest_framework import mixins, viewsets
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.reverse import reverse

from .models import Member, Partner
from .serializers import MemberSerializer, PartnerSerializer


class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    pass


class PartnerViewSet(CreateListRetrieveViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class MemberViewSet(CreateListRetrieveViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({

#     })
