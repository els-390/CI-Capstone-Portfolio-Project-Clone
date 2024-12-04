from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Review
from .forms import ReviewForm

class ReviewListView(ListView):
    model = Review
    template_name = 'review_list.html'  # Replace with your template
    context_object_name = 'reviews'
    
def review_list(request):
    """View to display all reviews."""
    reviews = Review.objects.all().order_by('-created_on')
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

class ReviewCreateView(CreateView):
    model = Review
    fields = ['review_title', 'content', 'rating']
    template_name = 'review_form.html'  # Replace with your template
    success_url = reverse_lazy('review_list')   

@login_required
def add_review(request):
    """View to allow logged-in users to add a review."""
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('reviews_list')
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {'form': form})


class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['title', 'content', 'rating']
    template_name = 'review_form.html'  # Reuse the form template for adding/editing reviews
    context_object_name = 'review'
    success_url = reverse_lazy('reviews:reviews_list')  # Ensure the URL is correctly named
    
    from django.views.generic.edit import DeleteView

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review_confirm_delete.html'  # Create this confirmation template
    context_object_name = 'review'
    success_url = reverse_lazy('reviews:reviews_list')  # Redirect after deletion
