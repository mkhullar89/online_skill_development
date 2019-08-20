from django.db import models
#
class Basemodel(models.Model):
    createad_at= models.DateTimeField();
    updated_at= models.DateTimeField();

    class Meta:
        abstract=True;