from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import date

from .models import Book, Member, Transaction
from .forms import BookForm, MemberForm, IssueForm


def login_page(request):
    if request.method == "POST":
        uname = request.POST["username"]
        pwd = request.POST["password"]
        user = authenticate(username=uname, password=pwd)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials")
    return render(request, "login.html")


def dashboard(request):
    books = Book.objects.count()
    members = Member.objects.count()
    transactions = Transaction.objects.count()
    return render(request, "dashboard.html", locals())


def add_book(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("view_books")
    return render(request, "add_book.html", {"form": form})


def view_books(request):
    books = Book.objects.all()
    return render(request, "view_books.html", {"books": books})


def issue_book(request):
    form = IssueForm()
    if request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['book']
            if book.available_quantity > 0:
                book.available_quantity -= 1
                book.save()
                form.save()
                return redirect("dashboard")
            else:
                messages.error(request, "Book not available")
    return render(request, "issue_book.html", {"form": form})


def return_book(request, id):
    t = Transaction.objects.get(id=id)
    t.return_date = date.today()

    # Fine Calculation
    if t.return_date > t.due_date:
        t.fine = (t.return_date - t.due_date).days * 5

    t.status = "Returned"
    t.book.available_quantity += 1
    t.book.save()
    t.save()
    return redirect("dashboard")
