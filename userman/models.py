from django.db import models
#


class Basemodel(models.Model):
    createad_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True;
