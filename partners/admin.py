from django.contrib import admin
from .models import Partner, Member

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
  pass

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
  pass
