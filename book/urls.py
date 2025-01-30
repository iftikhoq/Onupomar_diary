from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('book/<int:id>/', views.BookPage, name='bookpage'),
    path('borrow/<int:id>/', views.BorrowBook, name='borrow'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)