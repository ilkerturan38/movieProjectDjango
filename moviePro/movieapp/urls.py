
from unicodedata import name
from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name="index"),
    path('movieList',views.index,name="movieList"),
    path('movieDetail/<slug:slug>',views.movieDetail,name="movieDetail"),
    path('serialDetail/<slug:slug>',views.serialDetail,name="serialDetail"),
    path('cast/<slug:slug>',views.cast,name="cast"),
    path('director/<slug:slug>',views.director,name="director"),
    path('category/<slug:slug>',views.category,name="category"),
    path('pricingPlan',views.pricingPlan,name="pricingPlan"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('search',views.search,name="search"),
    path('filter',views.filter,name="filter"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
