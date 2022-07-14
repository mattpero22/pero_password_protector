from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from main_app.models import StoredAccount
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from main_app.forms import AccountForm
from main_app.static.scripts import encryption


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
  print(account.service, account.login, account.password)
  login_raw = encryption.decrypt(account.login, 'hello')
  password_raw = encryption.decrypt(account.password, 'hello')
  return render(request, 'vault/detail.html', { 'account': account, 'service': account.service, 'login': login_raw, 'password': password_raw })

@login_required
def add_account(request):
  user = request.user
  form = AccountForm(request.POST)
  # validate the form
  if form.is_valid():
    new_account = form.save(commit=False)
    new_account.user = user
    new_account.login = encryption.encrypt(new_account.login, 'hello')
    new_account.password = encryption.encrypt(new_account.password, 'hello')
    new_account.save()
  return redirect('/vault/', user_id=user)

@login_required
def confirm_user(request):
  pass

class AccountDelete(LoginRequiredMixin, DeleteView):
  model = StoredAccount
  success_url = '/vault/'

class AccountUpdate(LoginRequiredMixin, UpdateView):
  model = StoredAccount
  fields = ['service', 'login', 'password']
  success_url = '/vault/'
