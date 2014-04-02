from django.conf import settings
from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

from lookupip.apps.test1.views import *
import debug_toolbar

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lookupip.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', index),
)

#if settings.DEBUG:
#    import debug_toolbar
#    urlpatterns += patterns('',
#        url(r'^__debug__/', include(debug_toolbar.urls)),
#    )
