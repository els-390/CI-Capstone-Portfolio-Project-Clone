from django.urls import path
from .views import ReviewListView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView, add_review

app_name = 'reviews'

urlpatterns = [
    path('', ReviewListView.as_view(), name='reviews_list'),
    path('add/', add_review, name='add_review'),
    path('<int:pk>/edit/', ReviewUpdateView.as_view(), name='edit_review'),
    path('<int:pk>/delete/', ReviewDeleteView.as_view(), name='delete_review'),
]
