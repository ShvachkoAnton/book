from django.views.generic import ListView,DetailView
from django.db.models import Q
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class BookList(LoginRequiredMixin, ListView):
    model=Book
    template_name = 'books/book_list.html'
    context_object_name='book_list'

class BookDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView): # new
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    login_url='account_login'
    permission_required='books.special_status'

class SearchResult(ListView):
    model=Book
    context_object_name='book_list'
    template_name= 'books/search_results.html'
    def get_queryset(self):
        query=self.request.GET.get('q')
        return Book.objects.filter(
        Q(title__icontains=query)|Q(author__icontains=query)

        )



