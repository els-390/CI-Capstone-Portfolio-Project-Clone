from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProjectList.as_view(), name='home'),
    path('<slug:slug>/', views.project_detail, name="project_detail"),
    ]