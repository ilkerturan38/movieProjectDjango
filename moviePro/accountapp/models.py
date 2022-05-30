
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,verbose_name="Kullanıcı")
    image=models.FileField(upload_to="profile",verbose_name="Profil Resmi",blank=True)
    location=models.CharField(max_length=100,null=True,blank=True,verbose_name="Konum")

    class Meta:
        verbose_name="profile"
        verbose_name_plural="Profil"
        db_table="tblprofile"


# Sinyal'i algılayan obje,fonksiyon tanımlandı (İçerisinde Örn; User Modeli üzerinden save method'unu çalıştıktan sonra yapılacak işlemlere ait modeli tanımladık)
@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created, **kwargs): # instance = hangi user(kullanıcı) üzerinden yeni profil kaydı oluşucak (yeni bir User kaydı üzerinden,Profil bilgilerini kayıt etme)
    if created:   
        profile.objects.create(user=instance)


@receiver(post_save,sender=User) # Var olan User kaydı üzerinden Profile bilgilerini güncelleme işlemi
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()

