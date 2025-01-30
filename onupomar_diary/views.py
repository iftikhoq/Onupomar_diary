from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages 
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm 
from django.contrib.auth import login, authenticate, logout,update_session_auth_hash
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required


# def SignupPage(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             messages.success(request, f'Signup successful! Welcome, {user.username}.')
#             return redirect('login')
#         else:
#             messages.error(request, 'Signup failed. Please correct the errors below.')
#     else: 
#         form = SignupForm()
    
#     return render(request, 'signup.html', {'form': form}) 


# def LoginPage(request):
#     if request.method == 'POST':
#         form = LoginForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password) 
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, f"Welcome, {username}!")
#                 return redirect('profile')  
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Please fill out form correctly.")
#     else:
#         form = LoginForm()  
    
#     return render(request, 'login.html', {'form': form})

# def LogoutPage(request):
#     logout(request)
#     messages.success(request, "You have successfully logged out.")
#     return redirect('home')

# @login_required
# def ProfilePage(request):
#     return render(request, 'profile.html')

# class ChangePasswordView(PasswordChangeView):
#     template_name = 'changepasswithprev.html'
#     form_class = PasswordChangeForm
#     success_url = reverse_lazy('profile')

#     def form_valid(self, form):
#         form.save()
#         update_session_auth_hash(self.request, form.user)
#         messages.success(self.request, "You have successfully changed your password.")
#         return super().form_valid(form)

#     def form_invalid(self, form):
#         messages.error(self.request, "Please fill out the form correctly.")
#         return super().form_invalid(form)

# class UserLoginView(LoginView):
#     template_name = 'login.html' 
#     success_url = reverse_lazy('profile')
#     def form_valid(self, form):
#         messages.success(self.request, 'Logged in successfully')
#         return super().form_valid(form)

#     def form_invalid(self, form):
#         messages.error(self.request, 'Logged in information incorrect')
#         return super().form_invalid(form)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['type']= 'Login'
#         return context

#     def get_success_url(self):
#         return self.success_url