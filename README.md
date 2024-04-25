![PyPI - Version](https://img.shields.io/pypi/v/django-twitter-auth-manager?color=blue)
![GitHub License](https://img.shields.io/github/license/codesyntax/django-twitter-auth-manager%20)

# django-twitter-auth-manager

Manage Twitter OAuth 2.0 Authorization Code Flow with PKCE (User Context) authentication by an Django app and store necessary token and refresh token for future uses.

## Dependencies

This package depends on the Tweepy library, and Django framework as well as the Django's cache application.

## Limitations

The auth manage system is designed to use Twitters Free API plan. That's why uses OAuth 2.0 Authorization Code Flow with PKCE (User Context), for write procedures. So the limitation are set by Twitters Free plan:

- access token is valid only for 2 hours
- 1 environment
- up to 1500 posts per month
- 50 requests / 24 hours PER APP for tweets
- 25 requests / 24 hoursPER USER info

More details in: [https://developer.twitter.com/en/portal/products/free](https://developer.twitter.com/en/portal/products/free)

## Installation

To install `django-twitter-auth-manager` simply run:

```bash

   pip install django-twitter-auth-manager
```

## Configuration

We need to hook `django-twitter-auth-manager` into our project.

1. Put `django_uptime` into your `INSTALLED_APPS` at settings module:

```python

   INSTALLED_APPS = (
       # other apps
       "django_twitter_auth_manager",
   )
```

2. Include the desired url path into your projects main `urls.py` file:

```python

   from django.urls import include, path

   urlpatterns = [
      ...
      path('twitter/', include('django_twitter_auth_manager.urls')),
      ...
   ]
```

## Usage

1. Execute the "Authenticate your app" Django admin action from Access Token list panel
2. Follow the Oauth2 flow procedure
3. Once the first access token is saved, we can now use the Tweepy client:

```python
   from django_twitter_auth_manager.models import Access_token

   access_token = Access_token.objects.last()
   client = tweepy.Client(access_token.access_token)
   client.create_tweet(text="Hello World!", user_auth=False)
```

### Refresh token

In order to refresh the access token, you can do manually by triggering admin's "Refresh token" action or checking the validity an triggering automatically:

```python
   from django_twitter_auth_manager.models import Access_token
   from django_twitter_auth_manager.views import refresh_token

   access_token = Access_token.objects.last()

   if not access_token.is_valid():
      access_token = refresh_token()

   # Further actions
```
