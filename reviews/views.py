from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
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

# def comment_edit(request, slug, comment_id):
#     """
#     Display an individual comment for edit.

#     **Context**

#     ``project``
#         An instance of :model:`projects.Project`.
#     ``comment``
#         A single comment related to the project.
#     ``comment_form``
#         An instance of :form:`projects.CommentForm`
#     """
#     if request.method == "POST":

#         queryset = Project.objects.filter(status=1)
#         project = get_object_or_404(queryset, slug=slug)
#         comment = get_object_or_404(Comment, pk=comment_id)
#         comment_form = CommentForm(data=request.POST, instance=comment)

#         if comment_form.is_valid() and comment.author == request.user:
#             comment = comment_form.save(commit=False)
#             comment.project = project
#             comment.approved = False
#             comment.save()
#             messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
#         else:
#             messages.add_message(request, messages.ERROR,
#                                  'Error updating comment!')

#     return HttpResponseRedirect(reverse('project_detail', args=[slug]))


# def comment_delete(request, slug, comment_id):
#     """
#     Delete an individual comment.

#     **Context**

#     ``project``
#         An instance of :model:`projects.Project`.
#     ``comment``
#         A single comment related to the project.
#     """
#     queryset = Project.objects.filter(status=1)
#     project = get_object_or_404(queryset, slug=slug)
#     comment = get_object_or_404(Comment, pk=comment_id)

#     if comment.author == request.user:
#         comment.delete()
#         messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
#     else:
#         messages.add_message(request, messages.ERROR,
#                              'You can only delete your own comments!')

#     return HttpResponseRedirect(reverse('project_detail', args=[slug]))