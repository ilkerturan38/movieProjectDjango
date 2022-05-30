from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
from autoslug import AutoSlugField

class language(models.Model):
    name=models.CharField(verbose_name="Dil",max_length=50,null=False,blank=False)

    class Meta:
        verbose_name="language"
        verbose_name_plural="Diller"
        db_table="tbllanguage"

    def __str__(self):
        return self.name