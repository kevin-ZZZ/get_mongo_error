from django.conf.urls import url
from . import views

urlpatterns = [
    url('^index/$',views.index),
    url('^index2/$',views.index2),
    url('^submit/$',views.submit)
]