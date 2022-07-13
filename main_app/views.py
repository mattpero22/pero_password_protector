from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

@login_required
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



