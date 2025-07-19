from django.contrib import admin
from .models import Provider

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = [
        'npi', 'full_name', 'city', 'state', 
        'primary_taxonomy', 'created_at'
    ]
    
    list_filter = [
        'state', 'primary_taxonomy', 'credential', 'created_at'
    ]
    
    search_fields = [
        'npi', 'first_name', 'last_name', 'organization_name',
        'city', 'primary_taxonomy'
    ]
    
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': (
                'npi', 'first_name', 'middle_name', 'last_name',
                'organization_name', 'credential'
            )
        }),
        ('Address Information', {
            'fields': (
                'address_line_1', 'address_line_2', 'city', 
                'state', 'postal_code'
            )
        }),
        ('Contact Information', {
            'fields': ('phone', 'fax')
        }),
        ('Professional Information', {
            'fields': ('primary_taxonomy',)
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    # Custom method to display full name in the admin list view
    def full_name(self, obj):
        return obj.full_name
    full_name.short_description = 'Full Name'
    
    # Override get_queryset to optimize database access
    def get_queryset(self, request):
        return super().get_queryset(request).select_related()
    
    actions = ['make_verified']
    
    def make_verified(self, request, queryset):
        # here you can implement the logic to mark providers as verified
        count = queryset.count()
        self.message_user(request, f'{count} providers processed.')
    make_verified.short_description = "Mark selected providers as verified"