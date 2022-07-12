
from django.contrib import admin
from django.urls import path, include
from two_factor.urls import urlpatterns as tf_urls
from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('', include(tf_urls,)),
    path('', include(tf_twilio_urls,)),
    # path('account/', include('django.contrib.auth.urls')),
]
