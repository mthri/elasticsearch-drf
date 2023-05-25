from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin

from shop.models import User

class CustomAdmin(admin.AdminSite):
    site_header = _('سامانه فروش خودرو')
    site_title = _('سامانه فروش خودرو')


admin_site = CustomAdmin()

@admin.register(User, site=admin_site)
class UserAdmin(UserAdmin):
    search_fields = ('username', 'last_name')