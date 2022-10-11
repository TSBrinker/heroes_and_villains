from django.db import models
from super_types.models import SuperType

# Create your models here.
class Super(models.Model):
    name = models.CharField(max_length=40)
    alter_ego = models.CharField(max_length=40)
    primary_ability = models.CharField(max_length=100)
    secondary_ability = models.CharField(max_length=100)
    catchphrase = models.CharField(max_length=100)
    super_type = models.ForeignKey(SuperType, on_delete=models.CASCADE)
