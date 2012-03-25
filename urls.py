from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),
	(r'^$','blog.auth.views.login_user'),
	(r'^home$','blog.views.index'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$','auth.views.login_user'),
    url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/Users/Daniel/Documents/blog/blog/uploads/'}),
)
