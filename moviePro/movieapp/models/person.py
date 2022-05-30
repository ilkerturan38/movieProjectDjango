from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator,RegexValidator
from tomlkit import date
from .contact import contact
from autoslug import AutoSlugField
from datetime import date
import re

class person(models.Model):
    
    gender_list=( # Cinsiyet için,Liste tanımlandı
        ('M','Erkek'),
        ('F','Kadın'),
    )
    duty_list=(
        ('1','Görevli'),
        ('2','Oyuncu'),
        ('3','Yönetmen'),
        ('4','Senarist'),
    )

    # AttributeError: 'str' object has no attribute 'pattern' hatası verirse ; regex validator sorgularını silince düzeliyor.
    re_alpha = re.compile('[^\W\d_]+$', re.UNICODE)
    alpha = RegexValidator(re_alpha, 'Only alphabetic')
    # alphanumeric = RegexValidator(r'^[a-z\sA-Z]*$', 'Sadece Alfabetik karakter girişi yapabilirsiniz!') # utf8 kontrolü olmayan.

    nameSurname=models.CharField(verbose_name="Ad ve Soyad",max_length=60,validators=[alpha])
    image=models.ImageField(upload_to="person",verbose_name="Resim",null=False,blank=False)
    birthday=models.DateField(verbose_name="Doğum Tarihi",null=False,blank=False)
    gender=models.CharField(verbose_name="Cinsiyet",max_length=1,choices=gender_list) # cinsiyet içerisine gender_list'i aktardık

    duty_type=models.CharField(verbose_name="Görev Türü",max_length=1,choices=duty_list)
    contact=models.OneToOneField(contact,on_delete=models.CASCADE,null=False,blank=False,verbose_name="Adres")

    slug=AutoSlugField(populate_from='nameSurname',unique=True,null=True,db_index=True)

    # Method'a property özelliği verdik. Html sayfalarında oluşturduğumuz özellikleri çağırıp kullandık.
    @property
    def duty(self):
        return f"{self.duty_list[int(self.duty_type)-1][1]}" # sayfada gösterirken index'in -1 değerini vermessek bir üstte ki değeri gösterir.

    @property
    def agecalculator(self):
        tarih=self.birthday
        td = date.today()
        return td.year - tarih.year - ((td.month, td.day) < (tarih.month, tarih.day)) # Yaş Hesaplama
        
        
    def __str__(self): # karşı (Filmler) tablo içerisinde kayıt eklerken,Person tablosundaki istenilen ilişkili alanları gösterdik
        return f"{self.nameSurname} || {self.duty_list[int(self.duty_type)-1][1]}" 

    class Meta:
        verbose_name="person"
        verbose_name_plural="Personeller"
        db_table="tblperson"

    

