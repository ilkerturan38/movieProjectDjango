from tabnanny import verbose
from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
from autoslug import AutoSlugField

class country(models.Model):
    name=models.CharField(verbose_name="Ülke Adı",max_length=50,null=False,blank=False)

    class Meta:
        verbose_name="country"
        verbose_name_plural="Ülkeler"
        db_table="tblcountry"

    def __str__(self):
        return self.name