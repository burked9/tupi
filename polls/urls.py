from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
            url(r'^$', views.IndexView.as_view(), name='index'),
            url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
            url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
            url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
]

'''
url(r'^about/', views.about, name='about'),
url(r'^category/(?P<category_name_slug>[\w-]+)/$', views.category, name='category'),
##url(r'^polls/', include('polls.urls', namespace='polls')), 
##url(r'^admin/', admin.site.urls),

from django.urls import path
from django.contrib import admin
admin.autodiscover()
'''