from django.contrib import admin
from .views import get_handler, refresh_token
from .models import Access_token
from django.http import HttpResponseRedirect
from django.core.cache import cache


def new_token(modeladmin, request, queryset):
    refresh_token()

new_token.short_description="Refresh token"

def auth_flow(modeladmin, request, queryset):
    oauth2_user_handler = get_handler()
    url = oauth2_user_handler.get_authorization_url()
    cache.set("_client", oauth2_user_handler._client.__dict__)
    return HttpResponseRedirect(url)
auth_flow.short_description="Authenticate your app"


class Access_tokenAdmin(admin.ModelAdmin):
    list_display = ('is_valid','get_expire_date', 'token_type','scope')
    list_display_links = ('is_valid', 'get_expire_date')
    actions = [auth_flow, new_token]

admin.site.register(Access_token, Access_tokenAdmin)
