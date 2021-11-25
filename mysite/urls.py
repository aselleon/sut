"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import market
from market import views
from mysite import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('main_info/', include('market.urls')),
    path('main/', views.course_info,name='main_info'),
    path('dev_contact/', views.dev_contacts, name='dev_contact'),
    path('team_members/', views.team_members, name='team_members'),
    path('main_page/', views.main_page, name='main_page'),
    path('login_page/', views.login_page, name='login_page'),
    path('indexcat/', views.indexcat, name='indexcat'),

    path('', include('market.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
