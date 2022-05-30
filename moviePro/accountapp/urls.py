
from unicodedata import name
from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login',views.login,name="login"),
    path('login2',views.login2,name="login2"),
    path('sing-in',views.singin,name="sing-in"),
    path('sing-in2',views.singinIki,name="sing-in2"),
    path('change-password',views.changepassword,name="change-password"),
    path('profile', views.profile,name="profile"),
    path('profile2', views.profile2,name="profile2"),
    path('logout',views.cikis,name="logout"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 