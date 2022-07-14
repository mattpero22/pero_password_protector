from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account/signup/', views.signup, name='signup'),
    path('vault/', views.accounts_index, name='index'),
    path('vault/create', views.add_account, name='create'),
    path('vault/<int:storedaccount_id>', views.accounts_detail, name='detail'),

]

