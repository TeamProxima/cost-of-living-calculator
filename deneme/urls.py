from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:

    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'src.views.home', name='home'),
    url(r'^questions', 'src.views.run', name='run'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'search', 'src.views.search', name='search'),
)
