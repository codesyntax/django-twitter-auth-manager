![PyPI - Version](https://img.shields.io/pypi/v/django-twitter-auth-manager?color=blue)
![GitHub License](https://img.shields.io/github/license/codesyntax/django-twitter-auth-manager)

# django-twitter-auth-manager
Manage Twitter OAuth 2.0 Authorization Code Flow with PKCE (User Context) authentication by an Django app and store necessary token and refresh token for future uses.

Installation
------------

To install ``django-twitter-auth-manager`` simply run:

```bash

   pip install django-twitter-auth-manager
```

Configuration
-------------

We need to hook ``django-twitter-auth-manage`` into our project.

1. Put ``django_uptime`` into your ``INSTALLED_APPS`` at settings module:

```python

   INSTALLED_APPS = (
       # other apps
       "django_twitter_auth_manage",
   )
```

2. Include the desired url path into your projects main ``urls.py`` file:

```python

   from django.urls import include, path

   urlpatterns = [
      ...
      path('twitter/', include('django_twitter_auth_manage.urls')),
      ...
   ]
```
