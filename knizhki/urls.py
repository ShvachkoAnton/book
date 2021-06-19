from django.urls import path

from .views import BookList,BookDetailView,SearchResult
urlpatterns=[
path('', BookList.as_view(), name='book_list'),
path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
path('search/',SearchResult.as_view(),name='search_results')

]