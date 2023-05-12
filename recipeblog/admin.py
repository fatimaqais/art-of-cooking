from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'excerpt', 'author', 'created_on', 'status')
    list_filter = ('status', 'created_on')
    search_fields = ['title', 'category']
    summernote_fields = ('ingredients', 'direction')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'recipe', 'created_on', 'approved')
    search_fields = ['name', 'body', 'created_on']
    list_filter = ('approved', 'created_on')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
