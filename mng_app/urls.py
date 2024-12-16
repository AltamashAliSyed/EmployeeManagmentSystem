from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('home', views.home, name='home'),
    path('viewEmp/', views.viewEmp, name='viewEmp'),
    path('addEmp', views.addEmp, name='addEmp'),
    path('removeEmp', views.removeEmp, name='removeEmp'),
    path('filterEmp/', views.filterEmp, name='filterEmp'),
    path('updateEmp', views.updateEmp, name='updateEmp'),
    path('updateEmp2', views.updateEmp2, name='updateEmp2'),
    path('updateEmp3', views.updateEmp3, name='updateEmp3'),
    path('search', views.search, name='search'),
    path('', RedirectView.as_view(url='login/', permanent=False)),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('feedback/',views.feedback,name="feedback")
    ,
]