from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from main_app.models import StoredAccount
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from main_app.forms import AccountForm
from main_app.static.scripts import encryption

import environ
env = environ.Env()
environ.Env.read_env()
CIPHER = env('CIPHER')


def home(request):
    return render(request, 'home.html')

def signup(request):
  error_messages = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_messages = 'Invalid Info - Please Try Again'
  form = UserCreationForm()
  context = {
    'form': form, 
    'error_messages': error_messages
  }
  return render(request, 'registration/signup.html', context)

@login_required
def accounts_index(request):
  accounts = StoredAccount.objects.filter(user=request.user)
  account_form = AccountForm()
  return render(request, 'vault/index.html', { 'accounts': accounts, 'account_form': account_form } )

@login_required
def accounts_detail(request, storedaccount_id):
  account = StoredAccount.objects.get(id=storedaccount_id)
  return render(request, 'vault/detail.html', { 'account': account })

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

@login_required
def add_account(request):
  user = request.user
  # create the ModelForm using the data in request.POST
  form = AccountForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_account = form.save(commit=False)
    new_account.user = user
    new_account.login = encryption.encrypt(new_account.login, CIPHER)
    new_account.password = encryption.encrypt(new_account.password, CIPHER)
    new_account.save()
  return redirect('/vault/', user_id=user)


