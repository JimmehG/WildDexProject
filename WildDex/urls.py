from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$|^login/', views.login_user, name='login'),  # www.sydneywilddex.com.au/
    url(r'^about/$', views.about, name='about'),  # www.sydneywilddex.com.au/about
    # url(r'^add_user/$', views.add_user, name='add_user'),  # www.sydneywilddex.com.au/add_user
    # url(r'^add_animal/$', views.add_animal, name='add_animal'),
    # url(r'^submitted/$', views.submitted, name='submitted'),  # etc.
    # url(r'^table/$', views.table, name='table'),
    # url(r'^animal_table/$', views.animal_table, name='animal_table'),
    # url(r'^register/$', views.register, name='register'),
    # url(r'^edit_animal/(?P<animal_id>\d+0)/$', views.edit_animal, name='edit_animal'),
    url(r'^(?P<user>branchm)/add_carer/$', views.register, name='add_carer'),
    url(r'^(?P<user>\w+)/$', views.user_home, name='user_home'),
    url(r'^(?P<user>\w+)/add_animal/$', views.add_animal, name='add_animal'),
    url(r'^(?P<user>\w+)/edit_animal/(?P<animal_id>\d+)$', views.edit_animal, name='edit_animal'),
    url(r'^(?P<user>\w+)/animal_table/$', views.animal_table, name='animal_table'),
    url(r'^(?P<user>\w+)/about/$', views.about, name='about'),
    url(r'^$|^login/', views.logout_user, name='logout'),
]
