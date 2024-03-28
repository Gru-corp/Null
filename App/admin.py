from django.contrib import admin

from .models import *

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')
    search_fields = ('name', 'owner')

@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    
@admin.register(SubjectSocialNetwork)
class SubjectSocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('social_network', 'user', 'organization', 'url')
    search_fields = ('social_network', 'user', 'organization')