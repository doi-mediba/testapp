from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.todo_list),
    url(r'^detail/(?P<pk>[0-9])+/$', views.todo_detail, name="detail"),
]