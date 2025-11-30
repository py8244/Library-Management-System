from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_page, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("add_book/", views.add_book, name="add_book"),
    path("view_books/", views.view_books, name="view_books"),
    path("issue_book/", views.issue_book, name="issue_book"),
    path("return/<int:id>/", views.return_book, name="return_book"),
]
