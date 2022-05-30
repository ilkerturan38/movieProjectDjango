from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
from autoslug import AutoSlugField

from .serial import serial

class serialVideo(models.Model):
    title=models.CharField(verbose_name="Video Başlığı",max_length=100,blank=False,null=False)
    url=models.CharField(verbose_name="Video URL Adresi",max_length=200,blank=False,null=False)
    serial=models.ForeignKey(serial,on_delete=models.CASCADE,blank=False,null=False,verbose_name="Dizi ID",related_name="diziURL")

    class Meta:
        verbose_name="diziVideo"
        verbose_name_plural="Dizi Videolar"
        db_table="tblserialVideo"

    def __str__(self):
        return self.title