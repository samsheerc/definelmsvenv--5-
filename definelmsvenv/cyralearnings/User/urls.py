from django.urls import path, include
from . import views
from lmsmainapp.views import*
from User import views as api_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='loginu'),
    path('logout/', views.user_logut, name='logoutu'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('coursedesc/<int:id>', views.coursedesc,name="coursedesc"),
    path('vexam/', views.vexam, name='vexam'),
    # path('tutorial/', views.tutorial, name='vclass'),
    path('404/', views.error404, name='404'),
    path('vcourse/<int:id>', views.vcourse, name='vcourse'),
    path('vclass/<int:id>', views.vclass, name='vclass'),
    path('savecom/', views.save_data_comment, name='savecom'),
    # path('deleteco/', views.delete_data, name='deleteco'),
    # path('editco/', views.edit_data, name='editco'),

###################comment############################

]