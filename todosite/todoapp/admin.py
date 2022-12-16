from django.contrib import admin
from .models import Task, Note, Comment, Tag

# Custom admin model for Task
class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['description']}),
        ('Status & Tags', {'fields': ['completed', 'tags']}),
    ]

class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['content']}),
        ('On', {'fields': ['task']}),
    ]


# Register your models here.
admin.site.register(Task, TaskAdmin)
admin.site.register(Note)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)