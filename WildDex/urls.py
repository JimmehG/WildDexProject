from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$|^index/$', views.index, name='index'),  # www.sydneywilddex.com.au/
    url(r'^about/$', views.about, name='about'),  # www.sydneywilddex.com.au/about
    url(r'^add_user/$', views.add_user, name='add_user'),  # www.sydneywilddex.com.au/add_user
    url(r'^submitted/$', views.submitted, name='submitted'),  # etc.
    url(r'^table/$', views.table, name='table'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
]
