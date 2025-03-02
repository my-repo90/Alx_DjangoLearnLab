# myapp/urls.py
from django.urls import path
from . import views
from .views import Book_List, LibraryDetailView ,LoginView ,LogoutView ,RegisterView
from django.urls import path
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book
from .views import list_books


urlpatterns = [
    path('', views.Book_List, name='home'),
    path('', views.LibraryDetailView, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('books/add_book/', add_book, name='add_book'),
   
]
"views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="
"edit_book/"