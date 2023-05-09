from django.db import models

# Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES = (
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    priority = models.CharField(max_length=200, choices=PRIORITY_CHOICES)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
