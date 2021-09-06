from django import forms

from .models import Member, Partner


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        exclude = ['is_active', 'is_removed', 'on_created', 'on_updated']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Partner name'}),
            'gstin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Partner GST'}),
            'website_uri': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Agency Website'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Partner Phone'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Partner email'}),
        }


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        exclude = ['is_active', 'is_removed', 'on_created', 'on_updated']
        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Partner name'}),
            'name': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }
