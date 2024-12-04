from django.urls import path
from . import views

urlpatterns = [
    # Example of a single review view, using the `review` name.
    path('reviews/', views.ReviewListView.as_view(), name='reviews_list'),
    path('reviews/add/', views.add_review, name='add_review'),
]
