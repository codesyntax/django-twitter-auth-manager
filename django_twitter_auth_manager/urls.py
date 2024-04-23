from django.conf.urls import url, include
from .views import callback

urlpatterns = [
    url(r"^callback$", callback),
]