from rest_framework.serializers import ModelSerializer

from .models import Partner, Member


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        exclude = ['is_active', 'is_removed', 'on_created', 'on_updated']


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        exclude = ['is_active', 'is_removed', 'on_created', 'on_updated']
