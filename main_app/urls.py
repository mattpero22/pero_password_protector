from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account/signup/', views.signup, name='signup'),
    path('vault/', views.accounts_index, name='index'),
    path('vault/confirm', views.confirm_user, name='confirm'),
    path('vault/create', views.add_account, name='create'),
    path('vault/<int:storedaccount_id>', views.accounts_detail, name='detail'),
    path('vault/<int:pk>/delete/', views.AccountDelete.as_view(), name='delete'),
    path('vault/<int:pk>/update/', views.AccountUpdate.as_view(), name='update'),
]

