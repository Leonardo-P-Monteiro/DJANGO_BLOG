from django.contrib import admin
from django.http import HttpRequest
from site_setup.models import MenuLink, SiteSetup
# Register your models here.

# @admin.register(MenuLink)
# class MenuLinkAdmin(admin.ModelAdmin):
#     list_display = ('id', 'text', 'url_or_path',)
#     search_fields = ('id', 'text', 'url_or_path',)
#     list_display_links = ('id', 'text', 'url_or_path',)

class MenuLinkInLine(admin.TabularInline):
    model = MenuLink
    extra = 1



@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    # Where the fields will be boolean fields you don't need write it on the
    # lists. Because for default it will be shown on the admin display - even 
    # you don't want. This is on the "list_display".
    list_display = 'title', 'description', 'show_header', 'show_search', \
    'show_menu', 'show_description', 'show_pagination', 'show_footer'
    list_display_links = 'title', 'description', 'show_header', 'show_search', \
    'show_menu', 'show_description', 'show_pagination', 'show_footer'
    search_fields = 'title', 'description', 'show_header', 'show_search', \
    'show_menu', 'show_description', 'show_pagination', 'show_footer'
    inlines = MenuLinkInLine,



    def has_add_permission(self, request):
        return not SiteSetup.objects.exists()
        