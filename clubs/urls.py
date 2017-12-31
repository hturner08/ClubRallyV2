from django.urls import path
from . import views

app_name = 'clubs'
urlpatterns = [path('', views.home, name='index'),
path('<int:club_id>/', views.detail, name='detail'),
path('<int:club_id>/join',views.join, name='join'),
path('<int:club_id>/edit',views.editClub,name='edit'),
path('create/',views.createClub,name='create'),]
