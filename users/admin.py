from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'town', 'county', 'post_code', 'country', 'longitude', 'latitude', 'captcha_score', 'has_profile', 'is_active', 'timestamp', 'updated')
    search_fields = ('user__username', 'address', 'town', 'county', 'post_code', 'country')
    list_filter = ('has_profile', 'is_active')
    readonly_fields = ('timestamp', 'updated')

    fieldsets = (
        (None, {
            'fields': ('user', 'address', 'town', 'county', 'post_code', 'country', 'longitude', 'latitude')
        }),
        ('Additional Information', {
            'fields': ('captcha_score', 'has_profile', 'is_active', 'timestamp', 'updated'),
            'classes': ('collapse',),
        }),
    )
