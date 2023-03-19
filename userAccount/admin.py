from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from userAccount.models import Account


class AccountAdmin(UserAdmin):
    """Customize admin site to look better"""
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_admin')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)

