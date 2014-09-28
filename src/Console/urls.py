from django.conf.urls import patterns, url
from django.views.generic import TemplateView

import views

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='ConsoleHome'),
    url(r'^runcommand$', views.run_command, name='RunCommand'),
    url(r'^download/(?P<file_name>\S+)$', views.download_result_file, name="DownloadResultFile")
)