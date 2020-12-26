from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    Evaluation = models.CharField(max_length=200, null=False)
    year = models.IntegerField(null=False)
    star = models.IntegerField(null=False)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.name