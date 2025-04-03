from django.contrib import admin
from .models import Todo

# Register the Todo model to make it visible in Django Admin
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed')  # Add the fields you want to see in the list view
    search_fields = ('title',)  # Make the title searchable in the admin interface
    list_filter = ('completed',)  # Add filter options for the 'completed' field
