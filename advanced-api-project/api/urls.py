from django.urls import path
from . import views 
urlpatterns = [
    path('books/<int:pk>' , views.Book_Delete_View.as_view()),
    path('books/<int:pk>' ,views.Book_Retrieve_View.as_view()) ,
    path('books/<int:pk>' ,views.Book_Update_View.as_view()),
    path('books/' , views.Book_List_View.as_view()),
    path('books/' , views.Book_Create_View.as_view()),

]