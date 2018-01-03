"""ClubRallyV2 URL Configuration

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
from django.urls import path
from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from clubs import views
#Convention is to use a seperate URLconf for each app
urlpatterns = [
    path('', views.front, name='frontpage'),
    path('aboutus/',views.about, name='aboutus'),
    path('clubs/', include('clubs.urls',namespace="clubs")),
    path('myclubs/', views.index, name='home'),
    path('user/settings', views.me, name='me'),
    path('user/<int:user_id>', views.user, name='user'),
    path('admin/', admin.site.urls),]

#User Actions
urlpatterns += [
    url(r'^login/$', auth_views.login, {'template_name': 'clubs/login.html'}, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', auth_views.logout, {'next_page': ''}, name='logout'),
    url('user/me',views.user,name='user')
]
