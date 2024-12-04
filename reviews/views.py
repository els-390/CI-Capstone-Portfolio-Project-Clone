from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
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
    fields = ['title', 'content', 'rating']
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

def edit_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
            return redirect('reviews_list')  # Replace with your reviews list view name
        else:
            form = ReviewForm(instance=review)
            messages.add_message(request, messages.ERROR, 'Error updating review!')
    return render(request, 'reviews/edit_review.html', {'form': form})