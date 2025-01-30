from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages 
from .models import Book, Review, Category
from accounts.models import Borrow
from .form import ReviewForm

def BookPage(request, id):
    book = get_object_or_404(Book, id=id)
    reviews = Review.objects.filter(book=book)
    if request.method == 'POST':
        
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            messages.success(request, f'Review submitted.')
            return redirect('login')
        else:
            messages.error(request, 'Please fillup the data correctly.')
    else: 
        form = ReviewForm()
    
    return render(request, 'book.html', {'book': book, 'reviews': reviews, 'form': form}) 

def BorrowBook(request, id):
    book = get_object_or_404(Book, id=id)

    if Borrow.objects.filter(user=request.user, book=book, returned=False).exists():
        return redirect("bookpage", id=book.id)

    user_account = request.user.account 

    if user_account.balance > book.borrowing_price:
        user_account.balance -= book.borrowing_price
        user_account.save()
        Borrow.objects.create(
            user=request.user,
            book=book,
        )
    else:
        messages.error(request, f'Insufficient balance.')
        return redirect("bookpage", id=book.id)

    return render(request, 'book.html') 

def Home(request):
    category = request.GET.get('category')
    books = Book.objects.all()
    categories = Category.objects.all()
    if category:
        books = books.filter(genre=category)  
    return render(request, 'index.html', {'books': books, 'categories':categories})