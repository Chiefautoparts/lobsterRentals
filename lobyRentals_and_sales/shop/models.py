from django.db import models

# Create your models here.
class Product(models.Model):
	item = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250)
	description = models.TextField()
	image = models.ImageField()
	availablilty = models.BooleanField(default=True)
	stock = models.IntegerField()
	category = models.ForeignKey(Category, related_name="Category")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class Category(models.Model):
	title = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
