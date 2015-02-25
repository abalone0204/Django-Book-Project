from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import hello
from mysite.views import current_time
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    ('^hello/$', hello),
    ('^current_time/$', current_time),

)
