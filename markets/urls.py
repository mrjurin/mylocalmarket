from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^market/(?P<market_id>\d+)$', views.market_detail, name='detail'),
    url(r'^zip/(?P<zip>\d+)$', views.markets_within_zip, name='markets_within_zip'),
    url(r'^search/(?P<zip>\d+)$', views.search_page, name='search_page'),
    url(r'^$', views.search_page, name='search_page'),
]
