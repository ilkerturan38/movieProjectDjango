
from django.db import models
from .movie import movie

class photo(models.Model):
    title=models.CharField(verbose_name="Fotoğraf Başlığı",max_length=50,null=False,blank=False)
    photo=models.ImageField(upload_to="inmoviesPhoto",verbose_name="Fotoğraflar",null=False,blank="False")
    moviephoto=models.ForeignKey(movie,on_delete=models.CASCADE,verbose_name="Film ID")

    class Meta:
        verbose_name="photo"
        verbose_name_plural="fotograflar"
        db_table="tblphoto"

    def __str__(self):
        return f"{self.title} {self.photo},{self.moviephoto}" 