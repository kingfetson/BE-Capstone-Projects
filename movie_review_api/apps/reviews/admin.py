from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie_title', 'user', 'rating', 'created_date')
    list_filter = ('rating', 'created_date', 'movie_title')
    search_fields = ('movie_title', 'review_content', 'user__email')
    ordering = ('-created_date',)
    date_hierarchy = 'created_date'
    
    fieldsets = (
        ('Movie Information', {
            'fields': ('movie_title', 'rating')
        }),
        ('Review Content', {
            'fields': ('review_content', 'user')
        }),
        ('Timestamps', {
            'fields': ('created_date', 'updated_date'),
            'classes': ('collapse',)
        })
    )
    
    readonly_fields = ('created_date', 'updated_date')