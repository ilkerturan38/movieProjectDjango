
from asyncio.windows_events import NULL
from multiprocessing import context
import random
import datetime
from django.db.models import Q

#from .import filters
from .filters import movieFilter

# --------YÖNLENDİRMELER----------

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render

# --------------------------------

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # Sayfalama Kütüphanesi
from django.contrib import messages # Mesaj Kütüphanesi

# --------MODELLER----------------

from .models.movie import movie
from .models.person import person
from .models.genre import genre
from .models.language import language
from .models.country import country
from .models.series import series
from .models.serial import serial
from .models.episode import episode
from .models.commentX import commentX

# ----------FORM-----------------

from .forms import commentForm

#------------------------------------------------------------------------------------------------------------

def index(request):
    sorgu=movie.objects.all().order_by("title") # Foreign Key normal kullanımı
    sorgu2=serial.objects.all().order_by("title")

    # Vizyona girecek olan Filmler

    start_date = datetime.date(2022, 5, 1)
    end_date = datetime.date(2022, 6, 30)
    vizyon=movie.objects.filter(Q(date__gte=start_date), Q(date__lte=end_date))

    # Foreign Key ile Ters ilişkili kullanımı
    '''
    sorgu2=country.objects.get(name="Almanya").movieCountry.all()
    print(sorgu2)
    '''
    
    paginator=Paginator(sorgu,6)
    page = request.GET.get('page',1)
    try:
        context = paginator.page(page)
    except PageNotAnInteger :
        context = paginator.page(1)
    except EmptyPage:
        context = paginator.page(paginator.num_pages)
        
    '''
    islem2=NULL
    for item in sorgu: # sorgudan alınan değerde tek bir kayıt dönüyorsa for döngüsünü kullanma!
        for user in item.genre.all():
            islem2=user.name
            print(islem2)
    '''

    context={
        'context':context,
        'vizyon':vizyon,
        'diziler':sorgu2
    }
    
    return render(request,"movie/index.html",context)

#------------------------------------------------------------------------------------------------------------

def movieDetail(request,slug):
    sorgu=get_object_or_404(movie,slug=slug)
    
    serileriAl=NULL
    if sorgu.serie is not None: # gelen Film'e ait başka Serie'ler var ise ; filmler tablosundaki serie alanı boş değilse 
        sorgu2=series.objects.get(name=sorgu.serie).seriesMovie.all() # seriler tablosundaki film_adi = filmler tablosundaki sorgu.serie değerine eşit mi ?
        serileriAl=sorgu2 # film'e ait tüm serileri al

    movies = list(movie.objects.all())
    karisik = random.sample(movies, 4)

    yorum=sorgu.movieComment.all()
    print(yorum)

    form=commentForm(request.POST or None) # Sayfaya POST işlemi olduğunda form değişkeni'ni POST'tan gelen bilgiler ile doldur,POST yapılmamışsa formu boş olarak döndür
    if form.is_valid(): # Validasyon işlemi başarılı bir şekilde sağlanıyorsa is_valid=TRUE ise tabloya kayıt işlemini yap.

        '''
        gelenveri1=request.POST['nameSurname']
        gelenveri2=request.POST['email']
        gelenveri3=request.POST['mesaj']
        gelenveri4=request.POST['rating']
        '''
           
        gelenveri1=form.cleaned_data['nameSurname']
        gelenveri2=form.cleaned_data['email']
        gelenveri3=form.cleaned_data['mesaj']
        gelenveri4=form.cleaned_data['rating']

        newComment=commentX(nameSurname=gelenveri1,email=gelenveri2,mesaj=gelenveri3,movieID=sorgu,rating=gelenveri4)
        newComment.save()
        messages.add_message(request,messages.SUCCESS,'Yorum ekleme işlemi başarılı bir şekilde gerçekleştirildi..')

    context={
        "film":sorgu,
        "turler":sorgu.genre.all(),
        "diller":sorgu.language.all(),
        "ekip":sorgu.people.all(),
        "video":sorgu.filmURL.all(),
        "fotograflar":sorgu.photo_set.all(),
        "seriler":serileriAl,
        "karisik":karisik,
        "yorumlar":yorum,
        "form":form
    }
    return render(request,"movie/movieDetail.html",context)


#------------------------------------------------------------------------------------------------------------

def serialDetail(request,slug):
    sorgu=get_object_or_404(serial,slug=slug)
    
    context={
        "dizi":sorgu,
        "turler":sorgu.genre.all(),
        "diller":sorgu.language.all(),
        "ekip":sorgu.people.all(),
        "video":sorgu.diziURL.all(),
        "bolumler":sorgu.serialEpisode.all()
    }
    return render(request,"serial/serialDetails.html",context)

#------------------------------------------------------------------------------------------------------------

def cast(request,slug):
    sorgu=get_object_or_404(person,slug=slug,duty_type=2)
    sorgu2=sorgu.ekipFilm.all() # Oyuncu'ya göre Film getirme işlemi
    sorgu3=sorgu.ekipFilm.all().count()
    sorgu4=sorgu.ekipDizi.all().count()

    context={
        "person":sorgu,
        "film":sorgu2,
        "filmsayisi":sorgu3,
        "dizisayisi":sorgu4
    }
    return render(request,"movie/cast.html",context)

#------------------------------------------------------------------------------------------------------------

def director(request,slug):
    sorgu=get_object_or_404(person,slug=slug,duty_type=3)
    sorgu2=sorgu.ekipFilm.all() # Yönetmen'e göre Film getirme işlemi
    sorgu3=sorgu.ekipFilm.all().count()
    sorgu4=sorgu.ekipDizi.all().count()
   
    context={
        "person":sorgu,
        "filmler":sorgu2,
        "filmsayisi":sorgu3,
        "dizisayisi":sorgu4
    }
    return render(request,"movie/director.html",context)

#------------------------------------------------------------------------------------------------------------

def category(request,slug):

    # Yöntem 1
    
    sorgu=get_object_or_404(genre,slug=slug)
    sonuc=sorgu.movieCategory.all() # Ters İlişki
    
    '''
    # Yöntem 2
    sorgu=get_list_or_404(genre,slug=slug)

    sonuc=NULL
    for item in sorgu:
        sonuc=item.movieCategory.all() # category'e göre film getirme işlemi (Tek for döngülü işlem)
        print(sonuc)
    '''

    paginator=Paginator(sonuc,5)
    page = request.GET.get('page',1)
    try:
        context = paginator.page(page)
    except PageNotAnInteger :
        context = paginator.page(1)
    except EmptyPage:
        context = paginator.page(paginator.num_pages)
    
    context={
       'gelenkategori':sorgu,
       'context':context,
    }
    return render(request,"movie/category.html",context)

#------------------------------------------------------------------------------------------------------------

def search(request):
    gelendeger=request.GET.get("value",None)
    if gelendeger:
        sorgu=movie.objects.filter(title__contains=gelendeger)
        context={
                "sorgu":sorgu
        }
        return render(request,"movie/search.html",context)

#------------------------------------------------------------------------------------------------------------

def filter(request):
    sorgu=movie.objects.all()
    myFilter=movieFilter(request.GET,queryset=sorgu)
    sorgu=myFilter.qs

    gelendeger01=request.GET.get("genre",None)
    gelendeger02=request.GET.get("language",None)
    gelendeger03=request.GET.get("image_quality",None)


    if gelendeger01 or gelendeger02 or gelendeger03:
        context={
        "myFilter":myFilter,
        "sorgu":sorgu
        }
        return render(request,"movie/filter.html",context)

    context={
        "myFilter":myFilter,
    }
    return render(request,"movie/filter.html",context)

#------------------------------------------------------------------------------------------------------------

def pricingPlan(request):
    return render(request,"movie/pricingPlan.html")

#------------------------------------------------------------------------------------------------------------

def about(request):
    return render(request,"movie/about.html")

#------------------------------------------------------------------------------------------------------------

def contact(request):
    return render(request,"movie/contact.html")

#------------------------------------------------------------------------------------------------------------

def error_404(request, exception,template_name='404.html'):
    return render(request,template_name,status=404)

