from django.urls.base import reverse
from rest_framework import serializers

from .models import Partner, Member


class PartnerSerializer(serializers.ModelSerializer):
    # members_url = serializers.URLField(source='get_absolute_url', read_only=True)
    url = serializers.SerializerMethodField()
    members_url = serializers.SerializerMethodField()

    def get_url(self, obj):
        # return obj.get_absolute_url()
        return reverse('partner:update', kwargs={'pk': obj.pk})

    def get_members_url(self, obj):
        return reverse('partner:member-add', kwargs={'pk': obj.pk})

    class Meta:
        model = Partner
        exclude = ['is_active', 'is_removed', 'on_created', 'on_updated']


class MemberSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    partner = serializers.HiddenField(default='w')

    def get_url(self, obj):
        # return obj.get_absolute_url()
        return reverse('partner:member-update', kwargs={'pk': obj.partner.pk, 'mem_pk': obj.pk})

    class Meta:
        model = Member
        exclude = ['is_active', 'is_removed', 'on_created', 'on_updated']
