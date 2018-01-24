from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^amadon/$', views.index),
    url(r'^amadon/buy$', views.checkout),
    url(r'^amadon/amadon$', views.index),
]
print "url.py sub:", urlpatterns