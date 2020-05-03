from django.db import models

# Create your models here.
class Message(models.Model):
    user_input = models.TextField()

    def __str__(self):
        return self.user_input