from django.urls import path
from . import views 
urlpatterns = [
    #["books/create", "books/update", "books/delete"]
    path('books/delete/<int:pk>' , views.Book_Delete_View.as_view()),
    path('books/<int:pk>' ,views.Book_Retrieve_View.as_view()) ,
    path('books/update/<int:pk>' ,views.Book_Update_View.as_view()),
    path('books/' , views.Book_List_View.as_view()),
    path('books/create/' , views.Book_Create_View.as_view()),

]