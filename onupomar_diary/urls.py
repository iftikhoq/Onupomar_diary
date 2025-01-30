from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from book.views import Home
from django.conf.urls.static import static

urlpatterns = [
    path('', Home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('books/', include('book.urls')),
    # path('signup', views.SignupPage, name = 'signup'),
    # path('login', views.UserLoginView.as_view(), name = 'login'),
    # path('changepasswithprev/', views.ChangePasswordView.as_view(), name='changepasswithprev'),
    # path('logout/', views.LogoutPage, name='logout'),
    # path('profile/', views.ProfilePage, name='profile'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)