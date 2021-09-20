from django.db import models

class todo(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()


    def __str__(self):
    	return self.title

    	