from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TaskModel(models.Model):
    titlu = models.CharField(max_length=200)
    deskrisaun = models.TextField()
    kompleta = models.BooleanField(default=False)
    data_kria = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titlu
