from django.shortcuts import render
from django.views import generic
from .models import Project

# Create your views here.

class ProjectList(generic.ListView):
    queryset = Project.objects.filter(status=1)
    template_name = "projects/index.html"
    paginate_by = 6