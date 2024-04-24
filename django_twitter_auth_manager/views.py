import tweepy
from django.conf import settings
from .models import Access_token
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.cache import cache

TWITTER_CLIENT_ID = getattr(settings, 'TWITTER_CLIENT_ID', None)
TWITTER_CLIENT_SECRET = getattr(settings, 'TWITTER_CLIENT_SECRET', None)
TWITTER_CALLBACK_URI = getattr(settings, 'TWITTER_CALLBACK_URI', None)
TWITTER_SCOPE = getattr(settings, "TWITTER_SCOPE", ['tweet.write', 'users.read', 'tweet.read', 'offline.access'])


def get_handler():
    return tweepy.OAuth2UserHandler(
        client_id=TWITTER_CLIENT_ID,
        redirect_uri=TWITTER_CALLBACK_URI,
        scope=TWITTER_SCOPE,
        client_secret=TWITTER_CLIENT_SECRET
    )

def callback(request):
    _client = cache.get("_client")

    if _client:
        oauth2_user_handler = get_handler()
        oauth2_user_handler._client.__dict__ = _client
        access_token = oauth2_user_handler.fetch_token(
            request.build_absolute_uri()
        )
        Access_token(**access_token).save()

    return HttpResponseRedirect(reverse("admin:index"))
