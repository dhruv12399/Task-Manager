from django.conf.urls import url

from . import views
# from mysite.core import views as core_views
from django.contrib.auth import views as auth_views

app_name = 'manager_task'

urlpatterns = [

	url(r'^signup/$', views.signup, name='signup'),
	url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'manager_task/login.jinja'}, name='login'),
    url(r'^addtask/$', views.add_new_task, name='addtask'),
    url(r'^(?P<task_id>[0-9]+)/changestatus/$', views.change_status, name='changestatus'),
    url(r'^(?P<task_id>[0-9]+)/edittask/$', views.edit_task, name='edittask'),
    url(r'^(?P<task_id>[0-9]+)/deletetask/$', views.delete_task, name='deletetask'),
    url(r'^sort_name/$', views.sort_name, name='sort_name'),
    url(r'^sort_addedon/$', views.sort_addedon, name='sort_addedon'),
    url(r'^sort_completeby/$', views.sort_completeby, name='sort_completeby'),
    url(r'^tasks/$', views.TaskList.as_view()),
    url(r'^tasks/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view()),

]
