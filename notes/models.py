from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    modified = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title