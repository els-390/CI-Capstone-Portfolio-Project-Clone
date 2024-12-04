from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
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