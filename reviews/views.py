from django.views.generic import ListView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Review
from .forms import ReviewForm

class ReviewListView(ListView):
    model = Review
    template_name = 'review_list.html'
    context_object_name = 'reviews'
    
def review_list(request):
    reviews = Review.objects.filter(approved=True).order_by('-created_on')
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

class ReviewCreateView(CreateView):
    model = Review
    fields = ['review_title', 'content', 'rating']
    template_name = 'add_review.html'
    success_url = reverse_lazy('review')

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('review')
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {'form': form})

class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['review_title', 'content', 'rating']
    template_name = 'add_review.html'
    context_object_name = 'review'
    success_url = reverse_lazy('review')

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
            return HttpResponseRedirect(reverse('review'))
        else:
            messages.add_message(request, messages.ERROR, 'Error updating your review!')

    else:
        review_form = ReviewForm(instance=review)

    return render(request, 'reviews/edit_review.html', {'form': review_form, 'review': review})

class ReviewDeleteView(DeleteView):
    model = Review
    success_url = '/reviews/'

def review_delete(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own review!')

        return HttpResponseRedirect(reverse('review', args=[slug]))