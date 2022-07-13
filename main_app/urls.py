from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account/signup/', views.signup, name='signup'),
    path('vault/', views.accounts_index, name='index'),
    path('vault/', views.accounts_detail, name='detail'),
]

