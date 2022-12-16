from django.shortcuts import render, redirect
from django.views import View
from .models import Task, Note, Comment, Tag
from .forms import TaskForm, UpdateForm, NoteForm, CommentForm, TagForm

# Create your views here.
class TaskListView(View):
    """Handles homepage"""
    def get(self, request):
        """Display the index.html page with list of tasks"""
        pending_tasks = Task.objects.filter(completed=False).order_by('-id')
        completed_tasks = Task.objects.filter(completed=True).order_by('-id')
        form = TaskForm()

        return render(
            request=request,
            template_name='index.html',
            context={
                'pending_tasks': pending_tasks,
                'completed_tasks': completed_tasks,
                'task_form': form,
                }
            )

    def post(self, request):
        """Take form data and create a new task in the todo list"""
        form = TaskForm(request.POST)
        if form.is_valid():
            task_description = form.cleaned_data['description']
            if Task.objects.filter(description=task_description).count() == 0:
                Task.objects.create(description=task_description)

        # Redirect to the homepage
        return redirect('home')

class TaskDetailView(View):
    """Handles the details page"""
    def get(self, request, task_id):
        """Display the detail.html page with form to update the task"""
        task = Task.objects.get(id=task_id)
        update_form = UpdateForm(initial={'description': task.description})

        comments = Comment.objects.filter(task=task)
        comment_form = CommentForm()

        tags = task.tags.all()
        tag_form = TagForm()

        return render(
            request=request,
            template_name='detail.html',
            context={
                'update_form': update_form,
                'comment_form': comment_form,
                'tag_form': tag_form,
                'task': task,
                'comments': comments,
                'tags': tags,
                },
        )

    def post(self, request, task_id):
        """Take form data and update, delete or mark complete the specific task, comment or tag"""
        if 'update' in request.POST:
            form = UpdateForm(request.POST)
            if form.is_valid():
                task_description = form.cleaned_data['description']
                task = Task.objects.filter(id=task_id)
                task.update(description=task_description)
        elif 'comment' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment_content = form.cleaned_data['content']
                if Comment.objects.filter(content=comment_content).count() == 0:
                    task = Task.objects.get(id=task_id)
                    Comment.objects.create(content=comment_content, task=task)
        elif 'remove' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment_content = form.cleaned_data['content']
                Comment.objects.filter(content=comment_content).delete()

        elif 'tag' in request.POST:
            form = TagForm(request.POST)
            if form.is_valid():
                tag_name = form.cleaned_data['name']
                if Tag.objects.filter(name=tag_name).count() == 0:
                    Tag.objects.create(name=tag_name)
                tag = Tag.objects.get(name=tag_name)
                Task.objects.get(id=task_id).tags.add(tag)

        elif 'untag' in request.POST:
            form = TagForm(request.POST)
            if form.is_valid():
                tag_name = form.cleaned_data['name']
                tag = Tag.objects.get(name=tag_name)
                Task.objects.get(id=task_id).tags.remove(tag)

        else:
            task = Task.objects.filter(id=task_id)
            if 'complete' in request.POST:
                task.update(completed=True)
            elif 'pending' in request.POST:
                task.update(completed=False)    
            elif 'delete' in request.POST:
                task.delete()
            # Either way redirect to the homepage
            return redirect('home')

        # All else redirect to the detail page
        return redirect('task', task_id)
        

class NotesView(View):
    """Handles the notes page"""
    def get(self, request):
        """Display the notes.html page with list of notes"""
        notes = Note.objects.all().order_by('id')
        form = NoteForm()

        return render(
            request=request,
            template_name='notes.html',
            context={
                'note_list': notes,
                'note_form': form,
            },
        )

    def post(self, request):
        """Take form data and create or delete a note in the notes list"""
        form = NoteForm(request.POST)
        if form.is_valid():
            note_text = form.cleaned_data['text']
            if 'create' in request.POST:
                if Note.objects.filter(text=note_text).count() == 0:
                    Note.objects.create(text=note_text)
            elif 'delete' in request.POST:
                Note.objects.filter(text=note_text).delete()

        # Redirect to the todo homepage
        return redirect('notes')