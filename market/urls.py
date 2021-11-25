from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.course_info, name='course_info'),
    path('dev_contact/', views.dev_contacts, name='dev_contact'),
    path('team_members/', views.team_members, name='team_members'),
    path('main_page/', views.main_page, name='main_page'),
    path('login_page/', views.login_page, name='login_page'),
    path('catalogue/', views.product_list, name='catalogue'),
    path('indexcat/', views.indexcat, name='indexcat'),

    url(r'^$', views.product_list, name='product_list'),
    path('products/',
        views.product_list,
        name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),

]