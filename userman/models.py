from django.db import models
#


class Basemodel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserProfile(Basemodel):
    skills = models.CharField(max_length=500)
    interests = models.TextField()
    levels = models.IntegerField()
    projects = models.CharField(max_length=2000)

