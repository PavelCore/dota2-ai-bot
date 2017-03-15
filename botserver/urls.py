from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'reset', views.reset, name='reset'),
    url(r'select', views.select, name='select'),
    url(r'chat', views.chat, name='chat'),
    url(r'levelup', views.levelup, name='levelup'),
    url(r'update', views.update, name='update'),
]