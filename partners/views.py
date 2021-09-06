from django.shortcuts import render

from .forms import PartnerForm, MemberForm


def partner_home(request):
    return render(request, 'partners/list.html', {})


def add_partner(request, pk=None):
    partner_form = PartnerForm()
    if request.method == 'post':
        partner_form = PartnerForm(request.POST)
        if partner_form.is_valid():
            partner_form.save()

    return render(request, 'partners/update_partner.html', {
        'partner_form': partner_form
    })


def add_member(request, pk=None):
    member_form = MemberForm()
    if request.method == 'post':
        member_form = MemberForm(request.POST)
        if member_form.is_valid():
            member_form.save()

    return render(request, 'partners/update_partner.html', {
        'member_form': member_form
    })
