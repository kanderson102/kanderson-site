from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.project_list, name = "list"),
    url(r'^create/', views.project_create, name = "create"),
    url(r'^(?P<slug>[\w-]+)/$', views.project_detail, name = "detail"),
    url(r'^(?P<slug>[\w-]+)/edit/', views.project_update, name = "update"),
    url(r'^(?P<slug>[\w-]+)/delete/', views.project_delete, name = "delete"),
]
