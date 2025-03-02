from .models import Book, Author, Librarian, Library


library = Library.objects.get(name=Library)
librarian = Librarian.objects.get(library=Librarian)
"Library.objects.get(name=library_name)"
"books.all()"
Author.objects.get(name=Author)
"objects.filter(author=Author)"