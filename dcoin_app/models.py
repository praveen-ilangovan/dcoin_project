from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)

	def __str__(self):
		return '{0} {1}'.format(self.first_name, self.last_name)