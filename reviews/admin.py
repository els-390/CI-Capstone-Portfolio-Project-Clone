from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'client', 'review_title', 'project', 'rating', 'created_on', 'approved')
    list_filter = ('author', 'client', 'rating', 'created_on')
    search_fields = ('author', 'review_title', 'user__username', 'project', 'content')