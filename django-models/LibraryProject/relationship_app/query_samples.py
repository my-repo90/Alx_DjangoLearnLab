from .models import Book, Author, Librarian, Library

author = Author.objects.get(name=Author)
library = Library.objects.get(name=Library)
librarian = Librarian.objects.get(library=Librarian)
"Library.objects.get(name=library_name)"
"books.all()"