from django.urls import path
from .views import (
    ReviewListView,
    ReviewCreateView,
    ReviewUpdateView,
    ReviewDeleteView,
    add_review,
    edit_review,
    review_delete
)

urlpatterns = [
    path('', ReviewListView.as_view(), name='review'),
    path('add/', add_review, name='add_review'),
    path('<int:pk>/edit/', ReviewUpdateView.as_view(), name='review_edit'),
    path('<int:review_id>/edit-custom/', edit_review, name='edit_review'),
    path('<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
    path('<int:review_id>/delete-custom/', review_delete, name='delete_review'),
]
