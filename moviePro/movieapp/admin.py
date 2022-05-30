from asyncio.windows_events import NULL
from django.contrib import admin
from .models.movie import movie
from .models.person import person
from .models.country import country
from .models.genre import genre
from .models.language import language
from .models.video import video
from .models.contact import contact
from .models.series import series
from .models.photo import photo
from .models.commentX import commentX
from .models.serial import serial
from .models.serialVideo import serialVideo
from .models.episode import episode

# ------------------------------------------------------------------------------

class adminMovie(admin.ModelAdmin):
    list_display=['title','date','image_quality','tur','dil','ekip','bilgilendirme',]
    
    # ManytoMany ilişkili tablolardaki kayıtları admin panelinde gösterebilmek için fonksiyonlar tanımlandı
    def tur(self,gelendeger):
        sonuc=NULL
        for item in gelendeger.genre.all():
            sonuc=item.name
        return sonuc

    def ekip(self,gelendeger):
        sonuc=NULL
        for item in gelendeger.people.all():
            sonuc=item.nameSurname+" || "+item.duty
        return sonuc

    def dil(self,gelendeger):
        sonuc=NULL
        for item in gelendeger.language.all():
            sonuc=item.name
        return sonuc

    def tur(self,gelendeger):
        sonuc=NULL
        for item in gelendeger.genre.all():
            sonuc=item.name
        return sonuc

    def bilgilendirme(self,gelendeger):
        return f"Yaş Sınırı : {gelendeger.age_limit} yaş ~~ Film Süresi : {gelendeger.movie_time} Dakikadır."

admin.site.register(movie,adminMovie)

# ------------------------------------------------------------------------------

class adminPerson(admin.ModelAdmin):
    list_display=['nameSurname','birthday','gender','duty_type','contact',]

admin.site.register(person,adminPerson)

# ------------------------------------------------------------------------------

class adminCountry(admin.ModelAdmin):
    list_display=['name',]

admin.site.register(country,adminCountry)

# ------------------------------------------------------------------------------

class adminGenre(admin.ModelAdmin):
    list_display=['name',"slug"]
   

admin.site.register(genre,adminGenre)

# ------------------------------------------------------------------------------

class adminLanguage(admin.ModelAdmin):
    list_display=['name',]

admin.site.register(language,adminLanguage)

# ------------------------------------------------------------------------------

class adminVideo(admin.ModelAdmin):
    list_display=['title',]
    
admin.site.register(video,adminVideo)

# ------------------------------------------------------------------------------

class adminPhoto(admin.ModelAdmin):
    list_display=['title','photo']
    
admin.site.register(photo,adminPhoto)

# ------------------------------------------------------------------------------

class adminSeries(admin.ModelAdmin):
    list_display=['name',]
    
admin.site.register(series,adminSeries)

# ------------------------------------------------------------------------------

class adminEpisode(admin.ModelAdmin):
    list_display=['serial','title', ]

admin.site.register(episode,adminEpisode)

# ------------------------------------------------------------------------------

class adminSerial(admin.ModelAdmin):
    list_display=['title','date','slug','tur','dil','ekip','bilgilendirme',]

    def tur(self,gelendeger):
        sonuc=NULL
        for item in gelendeger.genre.all():
            sonuc=item.name
        return sonuc

    def ekip(self,gelendeger):
        sonuc=NULL
        for item in gelendeger.people.all():
            sonuc=item.nameSurname+" || "+item.duty
        return sonuc

    def dil(self,gelendeger):
        sonuc=NULL
        for item in gelendeger.language.all():
            sonuc=item.name
        return sonuc

    def tur(self,gelendeger):
        sonuc=NULL
        for item in gelendeger.genre.all():
            sonuc=item.name
        return sonuc

    def bilgilendirme(self,gelendeger):
        return f"Yaş Sınırı : {gelendeger.age_limit} yaş"


admin.site.register(serial,adminSerial)


# ------------------------------------------------------------------------------

class adminserialVideo(admin.ModelAdmin):
    list_display=['title',]
    
admin.site.register(serialVideo,adminserialVideo)

# ------------------------------------------------------------------------------

class adminComment(admin.ModelAdmin):
    list_display=['nameSurname','email','date','movieID']

admin.site.register(commentX,adminComment)

# ------------------------------------------------------------------------------

class adminContact(admin.ModelAdmin):
    list_display=['address','email','phone',]

admin.site.register(contact,adminContact)

# ------------------------------------------------------------------------------
