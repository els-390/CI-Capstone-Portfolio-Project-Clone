from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    """
    Stores a single review entry related to :model:`auth.User`
    and :model:`projects.Project`.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer")
    client = models.CharField(max_length=100)
    project = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField()  # Assuming a 1-5 star rating system
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.author}, {self.client}"