from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, TemplateView, RedirectView
from django.views.generic.edit import CreateView, UpdateView
from .models import Book
from .forms import BookForm


class MyLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('book_list')


class LoginRedirectView(RedirectView):
    pattern_name = 'login'

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['related_books'] = Book.objects.filter(author=self.object.author).exclude(id=self.object.id)
        return context


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_create.html'
    success_url = reverse_lazy('book_list')
    login_url = reverse_lazy('login')


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_update.html'
    success_url = reverse_lazy('book_list')
    login_url = reverse_lazy('login')


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
    login_url = reverse_lazy('login')

    permission_required = 'Book.delete_book'

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return super().handle_no_permission()
        else:
            return redirect(self.get_login_url())


class AboutView(TemplateView):
    template_name = 'about.html'
