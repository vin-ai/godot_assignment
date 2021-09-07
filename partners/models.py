from django.db import models
from django.urls import reverse


class Partner(models.Model):
    name = models.CharField('Partner Name', max_length=120, unique=True)
    gstin = models.CharField('Partner GST', max_length=15,
                             unique=True, null=True, blank=True)
    website_uri = models.URLField('Partner website', max_length=120)
    phone_number = models.CharField('Partner Phone', max_length=15)
    email = models.EmailField('Partner email')

    on_created = models.DateTimeField(auto_now_add=True)
    on_updated = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_removed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name.__str__()

    def get_absolute_url(self):
        return reverse("api:partner-detail", kwargs={"pk": self.pk})


class Member(models.Model):
    partner = models.ForeignKey(
        Partner, related_name='members', on_delete=models.PROTECT)
    name = models.CharField('Member Name', max_length=120)
    mobile_number = models.CharField('Mobile number', max_length=15)
    email = models.EmailField('Member email')

    on_created = models.DateTimeField(auto_now_add=True)
    on_updated = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_removed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.name)

    def get_absolute_url(self):
        return reverse("partner-member-update", kwargs={"partner_pk": self.partner.pk, 'pk': self.pk})
