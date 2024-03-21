from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.TextField(max_length = 10)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE )

    def __str__(self):
        return self.title