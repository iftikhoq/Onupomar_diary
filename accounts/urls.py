from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserAccountUpdateView, Changepasswithoutprev, LogoutPage, DepositPage, Profile
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutPage , name='logout'),
    path('profile/', Profile, name='profile' ),
    path('deposit/', DepositPage, name='deposit' ),
    path('changepasswithoutprev/', Changepasswithoutprev, name='changepasswithoutprev'),

]
