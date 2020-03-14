from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=30)
    info = models.CharField(max_length=200, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_at = models.DateTimeField("Due at")

    def __str__(self):
        return (self.title)
