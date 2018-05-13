from django.contrib import admin

from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    fields = ['title','author','text','created_date','published_date']
    search_fields = ['author']
    list_filter = ['author','title']
    list_display = ['author','title']
    list_editable = ['title']

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
