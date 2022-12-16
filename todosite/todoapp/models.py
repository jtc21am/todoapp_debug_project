from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.name
        
class Task(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.description

class Note(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.content