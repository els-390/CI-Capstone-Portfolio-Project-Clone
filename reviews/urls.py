from django.urls import path
from .views import ReviewListView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView, add_review

urlpatterns = [
    path('', ReviewListView.as_view(), name='review'),
    path('add/', add_review, name='add_review'),
    path('<int:pk>/edit/', ReviewUpdateView.as_view(), name='edit_review'),
    path('<int:pk>/delete/', ReviewDeleteView.as_view(), name='delete_review'),
]
