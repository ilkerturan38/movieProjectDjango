from tabnanny import verbose
from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
from autoslug import AutoSlugField
from .movie import movie

class video(models.Model):
    title=models.CharField(verbose_name="Video Başlığı",max_length=100,blank=False,null=False)
    url=models.CharField(verbose_name="Video URL Adresi",max_length=200,blank=False,null=False)
    movie=models.ForeignKey(movie,on_delete=models.CASCADE,blank=False,null=False,verbose_name="Film ID",related_name="filmURL")

    class Meta:
        verbose_name="video"
        verbose_name_plural="Videolar"
        db_table="tblvideo"

    def __str__(self):
        return self.title