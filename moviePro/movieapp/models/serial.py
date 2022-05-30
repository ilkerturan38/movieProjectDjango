from operator import ge
from tkinter import CASCADE
from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator,MaxValueValidator,MinValueValidator
from autoslug import AutoSlugField


from .person import person
from .country import country
from .language import language
from .genre import genre
from .series import series

class serial(models.Model):
    title=models.CharField(max_length=100,verbose_name="Dizi Adı",blank=False,null=False)
    description=models.TextField(validators=[MinLengthValidator(20)],verbose_name="Dizi Hakkında",null=False,blank=False)
    image=models.ImageField(upload_to="serial",verbose_name="Dizi Resmi",null=False,blank=False)
    date=models.DateField(verbose_name="Tarih",null=False,blank=False)
    slug=AutoSlugField(populate_from='title',unique=True,null=False,db_index=True)
    age_limit=models.PositiveIntegerField(verbose_name="Yaş Sınırı",validators=[MinValueValidator(7),MaxValueValidator(99)],null=False,blank=False)
    people=models.ManyToManyField(person,verbose_name="Dizi'nin Yetkilileri",related_name="ekipDizi")
    language=models.ManyToManyField(language,verbose_name="Dizi'nin Dili")
    country=models.ForeignKey(country,on_delete=models.CASCADE,verbose_name="Dizi'nin Çekildiği Ülke",related_name="serialCountry")
    genre=models.ManyToManyField(genre,verbose_name="Dizi Türü",related_name="serialCategory")

    class Meta:
        verbose_name="serial" 
        verbose_name_plural="Diziler"
        db_table="tblserial"

    def __str__(self):
        return f"{self.title} {self.date}"


