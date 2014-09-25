from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^polls/', include('polls.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    
    # Actually the above could be namespace="foo", then index.html needs
    # link to have "{% url 'foo:detail' question.id %}"
    
    url(r'^admin/', include(admin.site.urls)),
)
