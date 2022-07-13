from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# encrypt/decrypt pkgs
from Crypto.Cipher import AES
from Crypto import Random
import base64
import hashlib


class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    

class StoredAccount(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete = models.CASCADE, default=1)
    service = models.CharField(max_length=256)
    login = models.CharField(max_length=256) # encypt the user's login
    password = models.CharField(max_length=256) # encrypt the user's pw





