from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib import messages

from .models import Partner, Member
from .forms import PartnerForm, MemberForm


def partner_home(request):
    return render(request, 'partners/list.html', {})


def add_partner(request, pk=None):
    partner_form = PartnerForm()
    instance = None
    if pk:
        instance = get_object_or_404(Partner, id=pk)
        partner_form = PartnerForm(instance=instance)

    if request.method == 'POST':
        partner_form = PartnerForm(request.POST, instance=instance)
        if partner_form.is_valid():
            partner_form.save()
            messages.success(request, 'Partner addedd successfully!')

    api_post_endpoint = reverse('api:partner-list')
    submit_method = 'POST'

    if instance is not None:
        api_post_endpoint = reverse(
            'api:partner-detail', kwargs={'pk': instance.pk})
        submit_method = 'PUT'

    return render(request, 'partners/update_partner.html', {
        'partner_form': partner_form,
        'is_adding': 'yes' if instance is None else 'no',
        'api_post_endpoint': api_post_endpoint,
        'submit_method': submit_method,
    })


def add_member(request, pk, mem_pk=None):

    partner = get_object_or_404(Partner, id=pk)

    member_form = MemberForm(initial={'partner': pk})
    instance = None
    if mem_pk:
        instance = get_object_or_404(Member, id=mem_pk)
        member_form = MemberForm(instance=instance)

    if request.method == 'POST':
        member_form = MemberForm(request.POST, instance=instance)
        if member_form.is_valid():
            member_form.save()
            messages.success(request, 'Member addedd successfully!')

    api_url_member_list = api_post_endpoint = reverse('api:partner-members-list', kwargs={
        'partner_pk': partner.pk
    })
    submit_method = 'POST'

    if instance is not None:
        api_post_endpoint = reverse(
            'api:partner-members-detail', kwargs={
                'partner_pk': partner.pk,
                'pk': instance.pk
            })
        submit_method = 'PUT'

    return render(request, 'partners/update_member.html', {
        'partner_instance': partner,
        'member_form': member_form,
        'is_adding': 'yes' if instance is None else 'no',
        'api_post_endpoint': api_post_endpoint,
        'submit_method': submit_method,
        'api_url_member_list': api_url_member_list
    })
