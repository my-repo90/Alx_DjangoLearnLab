
from django.shortcuts import render
from .models import Book,Library
from django.views.generic import DetailView,CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required ,login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import BookForm
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User


# Create your views here.
def Book_List(request):

     books = Book.objects.all()  #to fectch all the book instances from the database
     context = {'book_list': books}  # Create a context dictionary with book list
     return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
  """A class-based view for displaying details of a specific library."""
  model = Library
  template_name = 'relationship_app/library_detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)  
    book = self.get_object() 
    context['average_rating'] = book.get_average_rating() 


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"

def LogoutView(request):
    return render(request, 'relationship_app/logout.html')

def LoginView(request):
    return render(request, 'relationship_app/login.html')

def Register(request):
    return render(request, 'relationship_app/register.html')

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True

def check_role(user, role):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role

@user_passes_test(lambda user: check_role(user, 'Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(lambda user: check_role(user, 'Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view
@user_passes_test(lambda user: check_role(user, 'Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Add book view
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request,'relationship_app/delete_book.html', {'book': book})

#UserCreationForm()
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
	
