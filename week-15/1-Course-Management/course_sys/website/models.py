from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length = 200, primary_key = True)
    description = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    @classmethod
    def exists(cls, name):
    	try:
    		u = cls.objects.get(name=name)
    		return True
    	except:
    		return False
