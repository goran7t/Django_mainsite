""" database models for mainsite """
from django.db import models

class Article(models.Model):
    """ Article table in database """
    #id = models.IntegerField(primary_key=True) #not needed, id is automatically added
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=2048)
