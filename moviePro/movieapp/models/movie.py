
from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator,MaxValueValidator,MinValueValidator
from autoslug import AutoSlugField


from .person import person
from .country import country
from .language import language
from .genre import genre
from .series import series


class movie(models.Model):

    quality_list=(
    ('1','4K'),
    ('2','1080P'),
    ('3','720P'),
    ('4','480P'),
    )
     
    title=models.CharField(max_length=100,verbose_name="Film Adı",blank=False,null=False)
    description=models.TextField(validators=[MinLengthValidator(20)],verbose_name="Film Hakkında",null=False,blank=False)
    image=models.ImageField(upload_to="movies",verbose_name="Film Resmi",null=False,blank=False)
    date=models.DateField(verbose_name="Tarih",null=False,blank=False)
    slug=AutoSlugField(populate_from='title',unique=True,null=False,db_index=True)
    movie_time=models.PositiveIntegerField(verbose_name="Film Süresi",validators=[MinValueValidator(35),MaxValueValidator(300)],null=False,blank=False)
    age_limit=models.PositiveIntegerField(verbose_name="Yaş Sınırı",validators=[MinValueValidator(7),MaxValueValidator(99)],null=False,blank=False)
    movie_budget=models.DecimalField(verbose_name="Film'in Bütçesi",max_digits=7,decimal_places=3) 
    # max_digits=girilecek maximum sayı, decimal_places=virgülden sonra ayrılcak olan kısım , max_value=10 min_value=1000 girilecek sayı aralığı 10-1000 arasında olmalı 
    people=models.ManyToManyField(person,verbose_name="Film'in Yetkilileri",related_name="ekipFilm")
    language=models.ManyToManyField(language,verbose_name="Film'in Dili")
    country=models.ForeignKey(country,on_delete=models.CASCADE,verbose_name="Film'in Vizyona Girdiği Ülke",related_name="movieCountry") # bir film yalnızca, bir ülkede vizyona girebilir
    genre=models.ManyToManyField(genre,verbose_name="Film Türü",related_name="movieCategory")
    serie=models.ForeignKey(series,on_delete=models.SET_NULL,blank=True,null=True,default=None,related_name="seriesMovie") # bir film yalnızca, bir Serie ait olabilir
    serieStatus=models.BooleanField(verbose_name="Seri Durumu",default=False)
    image_quality=models.IntegerField(verbose_name="Görüntü Kalitesi",choices=quality_list,blank=False,null=False)

    @property
    def kalite(self):
        return f"{self.quality_list[int(self.image_quality)-1][1]}"

    class Meta:
        verbose_name="movie" 
        verbose_name_plural="Filmler"
        db_table="tblmovie"

    def __str__(self):
        return f"{self.title} {self.date}"


