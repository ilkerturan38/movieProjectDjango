from tabnanny import verbose
from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
from autoslug import AutoSlugField
from django.core.validators import RegexValidator

class contact(models.Model):
    address=models.TextField(verbose_name="Adres Bilgisi",validators=[MinLengthValidator(20),MaxLengthValidator(100)],blank=False,null=False)
    email=models.EmailField(verbose_name="E-mail",max_length=30,blank=False,null=False)
    phone=models.CharField(verbose_name="Telefon",max_length=11,null=False,blank=False,validators=[
      RegexValidator(
        regex=r'^\+?1?\d{10,11}$',
        message="Phone number must be entered in the format '05325165796'. Up to 11 digits allowed."
      ),
    ],)

    class Meta:
        verbose_name="contact"
        verbose_name_plural="İletişim"
        db_table="tblcontact"

    def __str__(self):
        return f"{self.address} {self.email} {self.phone}"