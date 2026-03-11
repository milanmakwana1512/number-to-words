from django.db import models

class History(models.Model):

    number = models.CharField(max_length=50)

    words = models.TextField()

    date = models.DateTimeField(auto_now_add=True)