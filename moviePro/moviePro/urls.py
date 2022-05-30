
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('movieapp.urls')),
    path('account/',include('accountapp.urls')),
]

handler404 = 'movieapp.views.error_404'