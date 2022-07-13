
from django.contrib import admin
from django.urls import path, include
from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
    path('', include('main_app.urls')),
    path('', include(tf_urls,)),
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
]
