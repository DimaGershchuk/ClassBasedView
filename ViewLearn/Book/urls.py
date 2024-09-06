from django.urls import path
from .views import AboutView, BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, MyLoginView, LoginRedirectView

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('', AboutView.as_view(), name='about'),
    path('books/', BookListView.as_view(), name='book_list'),  # URL для списку книг
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),  # URL для деталей книги
    path('add/', BookCreateView.as_view(), name='book_create'),  # URL для створення книги
    path('<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),  # URL для оновлення книги
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),  # URL для видалення книги
    path('about/', AboutView.as_view(), name='about'),  # URL для сторінки "Про нас"
    path('redirect-login/', LoginRedirectView.as_view(), name='redirect_login'),

]