from django.db import models



class AsmrVideo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    datePublished = models.DateTimeField()
    embed = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
# Create your models here.
