from django.db import models
from django.utils.timezone import now
from django.core.validators import MinLengthValidator,MaxLengthValidator,MaxValueValidator,MinValueValidator
from .movie import movie
from .serial import serial

class commentX(models.Model):
    movieID=models.ForeignKey(movie,on_delete=models.CASCADE,null=False,blank=False,related_name="movieComment")
    serialID=models.ForeignKey(serial,on_delete=models.CASCADE,null=False,blank=False,related_name="serialComment")
    nameSurname=models.CharField(verbose_name="Yorum Yapan Kişi",max_length=30,null=False,blank=False)
    mesaj=models.TextField(verbose_name="Yapılan Yorum",validators=[MinLengthValidator(20)],blank=False,null=False)
    email=models.EmailField(verbose_name="E-mail",blank=False,null=False)
    date=models.DateTimeField(verbose_name="Yorum Yapılan Tarih",auto_now_add=True)
    rating=models.IntegerField(verbose_name="Puan")

    class Meta:
        verbose_name="comment"
        verbose_name_plural="Yorumlar"
        db_table="tblcomment"

    def __str__(self):
        return f"{self.nameSurname} {self.email} {self.movieID}"
