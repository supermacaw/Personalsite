from django.db import models

# Create your models here.
class PotentialMatch(models.Model):
	name = models.CharField(max_length=30)
	gender = models.CharField(max_length=1)
	MBTItype = models.CharField(max_length=4)
	fbURL = models.URLField()

	def __unicode__(self):
		return self.name
