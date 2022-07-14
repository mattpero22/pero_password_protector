from django.forms import ModelForm
from .models import StoredAccount

class AccountForm(ModelForm):
  class Meta:
    model = StoredAccount
    fields = ['service', 'login', 'password']