from django.db import models


class Player(models.Model):
	"""
	Player object
	Fields:
	name [string]
	address [string]
	points [integer]
	age [integer]

	"""
	name = models.CharField(max_length=60)
	address = models.CharField(max_length=60)
	points = models.IntegerField(default = 0)
	age = models.IntegerField(default = 1)

	def __str__(self):
		return self.name
