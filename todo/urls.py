from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.todo_list),
    url(r'^new$', views.todo_new, name="new"),
    url(r'^detail/(?P<pk>[0-9])+/$', views.todo_detail, name="detail"),
    url(r'^edit/(?P<pk>[0-9])+/$', views.todo_edit, name="edit"),    
]