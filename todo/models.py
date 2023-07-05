from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)  
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo-detail', kwargs={'pk': self.pk})
