from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from main_app.static.scripts import encryption

class StoredAccount(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
    service = models.CharField(max_length=256)
    login = models.CharField(max_length=256) # encypt the user's login
    password = models.CharField(max_length=256) # encrypt the user's pw
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.service

class CreateAccount(LoginRequiredMixin, CreateView):
    model = StoredAccount
    fields = ['service', 'login', 'password']
    success_url = '/vault/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def clean(self):
        cleaned_data = super().clean()
        login = cleaned_data.get("login")
        password = cleaned_data.get("password")





