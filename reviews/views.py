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
    reviews = Review.objects.all().order_by('-created_on')
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

class ReviewCreateView(CreateView):
    model = Review
    fields = ['review_title', 'content', 'rating']
    template_name = 'add_review.html'
    success_url = reverse_lazy('review_list')

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('review_list')
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {'form': form})

class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['review_title', 'content', 'rating']
    template_name = 'add_review.html'
    context_object_name = 'review'
    success_url = reverse_lazy('review_list')

@login_required
def edit_review(request, review_id):
    if request.method == "POST":
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.review = review
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating your review!')

    return HttpResponseRedirect(reverse('review_list'))

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review_list.html'
    context_object_name = 'review'
    success_url = reverse_lazy('review_list')

def review_delete(request, review_id):
    queryset = Review.objects.filter(status=1)
    review = get_object_or_404(queryset)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own review!')

    return HttpResponseRedirect(reverse('review_list'))
