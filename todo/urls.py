from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home$', views.home, name='home'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^about$', views.about, name='about'),
    url(r'^details/(?P<id>\w{0,50})/$', views.details, name='details'),
    url(r'^add$', views.add, name='add'),
    url(r'^signup/$', views.signup, name='signup'),
]
