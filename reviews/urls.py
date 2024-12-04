from django.urls import path
from . import views

urlpatterns = [
    # Example of a single review view, using the `review` name.
    path('reviews/', views.ReviewDetailView.as_view(), name='review'),
    path('reviews/add/', views.add_review, name='add_review'),
]
