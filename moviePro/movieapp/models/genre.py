from tabnanny import verbose
from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
from autoslug import AutoSlugField

class genre(models.Model):
    name=models.CharField(verbose_name="Film Türü",max_length=50,null=False,blank=False)
    slug=AutoSlugField(populate_from='name',unique=True,null=False,db_index=True,)

    class Meta:
        verbose_name="genre"
        verbose_name_plural="Türler"
        db_table="tblgenre"

    def __str__(self):
        return self.name