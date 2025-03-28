from django.db import models
from django.utils import timezone

class todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.CharField(max_length=30, default=timezone.now)



    def __str__(self):
        return self.title


