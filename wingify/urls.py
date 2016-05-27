from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.authtoken import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wingify.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^store/', include('store.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token)
)

urlpatterns += staticfiles_urlpatterns()
admin.site.site_header = 'Wingify'
