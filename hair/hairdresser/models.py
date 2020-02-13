from django.db import models

class Hairdresser(models.Model):
  name = models.CharField(max_length=50)
  about = models.CharField(max_length=200)
  image = models.CharField(max_length=500)

  def __str__(self):
    return self.name

class Services(models.Model):
  hairdresser = models.ForeignKey(Hairdresser, on_delete=models.CASCADE)
  description = models.CharField(max_length=500)
  prices =  models.IntegerField(default=0)
  
  def __str__(self):
    return self.hairdresser
  