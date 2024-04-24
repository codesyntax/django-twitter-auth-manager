from django.contrib import admin
from .views import get_handler
from .models import Access_token
from django.http import HttpResponseRedirect
from django.core.cache import cache


def refresh_token():
    oauth2_user_handler = get_handler()
    access_token = Access_token.objects.last()
    new_access_token = oauth2_user_handler.refresh_token('https://api.twitter.com/2/oauth2/token', refresh_token=access_token.refresh_token)

    token_obj = Access_token(**new_access_token)
    token_obj.save()
    return token_obj

def auth_flow(modeladmin, request, queryset):
    oauth2_user_handler = get_handler()
    cache.set("oauth2_user_handler", oauth2_user_handler)
    return HttpResponseRedirect(oauth2_user_handler.get_authorization_url())
auth_flow.short_description="Authenticate your app"


class Access_tokenAdmin(admin.ModelAdmin):
    list_display = ('token_type', 'scope', 'expires_at')
    actions = [auth_flow]

admin.site.register(Access_token, Access_tokenAdmin)
