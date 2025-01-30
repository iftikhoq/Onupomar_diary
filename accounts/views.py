from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm,UserUpdateForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.forms import SetPasswordForm 
from django.core.mail import send_mail
from django.contrib import messages 
from .forms import DepositForm
from .models import Borrow, Deposit

class UserRegistrationView(FormView):
    template_name = 'registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form) 
    

class UserLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('home')

def LogoutPage(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')

class UserAccountUpdateView(View):
    template_name = 'profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile') 
        return render(request, self.template_name, {'form': form})
    
    
def Changepasswithoutprev(request):
    if request.method  ==  'POST':
        form = SetPasswordForm(request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(request.user)
    return render(request, 'changepasswithoutprev.html', {'form': form}) 

def DepositPage(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            depo = form.save(commit=False)
            depo.user = request.user
            depo.save()
            
            user_account = request.user.account 
            user_account.balance += depo.amount
            user_account.save()

            messages.success(request, f'Amount deposited.')
            return redirect('login')
        else:
            messages.error(request, 'Please enter amount less than 5000.')
    else: 
        form = DepositForm()
    
    return render(request, 'deposit.html', {'form': form}) 

def Profile(request):
    borrows = Borrow.objects.filter(user=request.user.id)  
    deposits = Deposit.objects.filter(user=request.user.id)  
    
    return render(request, 'profile.html', {'borrows': borrows, 'deposits': deposits}) 