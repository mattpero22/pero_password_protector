from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class StoredAccount(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
    service = models.CharField(max_length=256)
    login = models.CharField(max_length=256) # encypt the user's login
    password = models.CharField(max_length=256) # encrypt the user's pw
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.service






