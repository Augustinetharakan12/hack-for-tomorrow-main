from django.db import models
from django import forms

class Photo(models.Model):
	title = models.CharField(max_length=255, blank=True)
	file = models.FileField(upload_to='photos/nsfw')
	uploaded_at = models.DateTimeField(auto_now_add=True)

class Result(models.Model):
	file_name = models.CharField(max_length=255, blank=True)
	file_url = models.CharField(max_length=255, blank=True)
	percentage_safe = models.FloatField(blank=True)