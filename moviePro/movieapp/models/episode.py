from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator,MaxValueValidator,MinValueValidator
from .serial import serial

class episode(models.Model):
    title=models.CharField(verbose_name="Bölüm Adı",max_length=200,blank=False,null=False)
    serial=models.ForeignKey(serial,on_delete=models.CASCADE,related_name="serialEpisode")
    url=models.CharField(verbose_name="Video URL Adresi",max_length=200,blank=False,null=False)
    episode_time=models.PositiveIntegerField(verbose_name="Bölüm Süresi",validators=[MinValueValidator(35),MaxValueValidator(300)],null=False,blank=False)
    release_date=models.DateField(verbose_name="Yayınlanma Tarihi",null=True,blank=True)
    
    class Meta:
        verbose_name="episode"
        verbose_name_plural="Bölümler"
        db_table="tblEpisode"