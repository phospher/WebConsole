from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import Console.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WebConsole.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('Console.urls'))
)
