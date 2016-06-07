from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_user/$', views.register, name='add_user'),
    url(r'^reg_type/$', views.reg_user_type, name='reg_type'),
    url(r'^add_carer/$', views.add_carer, name='add_carer'),
    url(r'^add_animal/$', views.add_animal, name='add_animal'),
    url(r'^pick_up/(?P<animal_id>\d+)$', views.pick_up, name='pick_up'),
    url(r'^check/$', views.check, name='check'),
    # url(r'^submitted/$', views.submitted, name='submitted'),  # etc.
    # url(r'^table/$', views.table, name='table'),
    url(r'^view_animal/(?P<animal_id>\d+)$', views.view_animal, name='view_animal'),
    url(r'^branch_animal_table/$', views.branch_animal_table, name='branch_animal_table'),
    url(r'^office_animal_table/$', views.animal_table, name='office_animal_table'),
    url(r'^carer_animal_table/$', views.carer_animal_table, name='carer_animal_table'),
    url(r'^carer_edit_animal/(?P<animal_id>\d+)$', views.carer_edit_animal, name='carer_edit_animal'),
    url(r'^office_edit_animal/(?P<animal_id>\d+)$', views.office_edit_animal, name='office_edit_animal'),
    url(r'^branch_edit_animal/(?P<animal_id>\d+)$', views.branch_edit_animal, name='branch_edit_animal'),
    # url(r'^register/$', views.register, name='register'),
    # url(r'^edit_animal/(?P<animal_id>\d+0)/$', views.edit_animal, name='edit_animal'),
    # url(r'^(?P<user>branchm)/add_carer/$', views.register, name='add_carer'),
    # url(r'^(?P<user>\w+)/$', views.user_home, name='user_home'),
    # url(r'^(?P<user>\w+)/add_animal/$', views.add_animal, name='add_animal'),
    # url(r'^(?P<user>\w+)/edit_animal/(?P<animal_id>\d+)$', views.edit_animal, name='edit_animal'),
    # url(r'^(?P<user>\w+)/animal_table/$', views.animal_table, name='animal_table'),
    # url(r'^(?P<user>\w+)/about/$', views.about, name='about'),
    # url(r'^$|^login/', views.logout_user, name='logout'),
]
