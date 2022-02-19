from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sharonstylists', views.sharonstylists, name='sharonstylists'),
    path('sharondesigners', views.sharondesigners, name='sharondesigners'),
    path('sharonfaceart', views.sharonfaceart, name='sharonfaceart'),
    path('contactsharon', views.contactsharon, name='contactsharon'),
    path('historysharon', views.historysharon, name='historysharon')

]