from django.db import models
from django.contrib.auth.models import User



class AsmrCategory(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.title

class AsmrCreator(models.Model):
    name = models.CharField(max_length=200)
    dateJoined = models.DateField()
    def __str__(self):
        return self.name

class AsmrVideo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    datePublished = models.DateTimeField()
    embed = models.CharField(max_length=1000)
    category = models.ForeignKey(AsmrCategory, verbose_name="Category", default=1, on_delete=models.SET_DEFAULT)
    creator = models.ForeignKey(AsmrCreator, verbose_name="Creator", default=1, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class UserVideoListEntry(models.Model):
    #what I think this will do is when a user is deleted, the corresponding User list entry in the database is deleted.
    #which makes sense in this scenario. If either the user or the video is deleted there doesn't need to be an entry for a video
    #in their list.
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    video = models.ForeignKey(AsmrVideo, verbose_name="Video", on_delete=models.CASCADE)
# Create your models here.
