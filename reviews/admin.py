from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'client', 'title', 'project', 'rating', 'created_on', 'approved')
    list_filter = ('author', 'client', 'rating', 'created_on')
    search_fields = ('author', 'title', 'user__username', 'project', 'content')