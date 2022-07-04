from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from tasks import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('add-todo', views.add_todo),
    path('logout', views.signout, name='signout'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('complete/<str:id>/<str:status>', views.complete, name='complete'),
    



]
