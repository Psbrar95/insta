"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path
from insta import views
from django.conf.urls import url
from django.conf.urls.static import static

from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/$',views.user_login,name="user_login"),
    url(r'^home/$',views.home,name="user_home"),
    url(r'^home/(?P<pk>\d+)/$',views.home, name='home_with_pk'),
    url(r"^logout/$",views.user_logout,name="user_logout"),
    path('change_friends/<operation>/<int:pk>', views.change_friends,name='change_friends'),
    url(r'^follower/(?P<pk>\d+)/$',views.follower,name='follower'),
    url(r'^following/(?P<pk>\d+)/$',views.following,name='following'),
    path('signup/',views.signup,name='signup'),
    path('addpost/',views.addpost,name = 'addpost'),
    path('alluserpost/',views.alluserpost,name='alluser_post'),
    path('',views.alluserpost),
    path('search/',views.search,name='search'),
 

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)