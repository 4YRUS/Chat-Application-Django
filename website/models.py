from django.db import models

class CreateRoom(models.Model):
	name=models.CharField(max_length=200)
	slug=models.SlugField(unique=True)
	
class Message(models.Model):
	username=models.CharField(max_length=50)
	value=models.CharField(max_length=200)
	slug=models.SlugField(max_length=50)


