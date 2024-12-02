from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Project
from .forms import CommentForm
# from .forms import CommentForm

# Create your views here.

class ProjectList(generic.ListView):
    queryset = Project.objects.filter(status=1)
    template_name = "projects/index.html"
    paginate_by = 6
    

def project_detail(request, slug):
    """
    Display an individual :model:projects.Project`.

    **Context**

    ``project``
        An instance of :model:`projects.Project`.

    **Template:**

    :template:`projects/project_detail.html`
    """
    queryset = Project.objects.filter(status=1)
    project = get_object_or_404(queryset, slug=slug)
    comments = project.comments.all().order_by("-created_on")
    comment_count = project.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.project = project
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
    )
        
    
    comment_form = CommentForm()

    return render(
    request,
    "projects/project_detail.html",
    {
        "project": project,
        "comments": comments,
        "comment_count": comment_count,
    },
)