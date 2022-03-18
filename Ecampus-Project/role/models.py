from django.db import models

# Create your models here.
class Role(models.Model):
    roleId = models.IntegerField(primary_key=True)
    roleName = models.CharField(max_length=50)
    class Meta: 
        verbose_name_plural = "Role"