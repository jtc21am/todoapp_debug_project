
from django.urls import path
from .views import TaskListView, TaskDetailView, NotesView

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
    path('notes/', NotesView.as_view(), name='notes'),
    path('<str:task_id>/', TaskDetailView.as_view(), name='task'),
]