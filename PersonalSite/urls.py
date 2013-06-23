from django.conf.urls import patterns, include, url
import sys
sys.path.append("..")
from MatchMaker.views import home_page
from MatchMaker.views import create_and_match

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PersonalSite.views.home', name='home'),
    # url(r'^PersonalSite/', include('PersonalSite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', home_page),
    url(r'^matchmaker/potentialmatch/$', create_and_match)
)
