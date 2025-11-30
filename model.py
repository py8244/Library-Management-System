from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20)
    quantity = models.IntegerField()
    available_quantity = models.IntegerField()

    def __str__(self):
        return self.title


class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    fine = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default="Issued")

    def __str__(self):
        return f"{self.book.title} → {self.member.name}"
