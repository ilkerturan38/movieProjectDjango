
from .models import profile
from dataclasses import field
from distutils.command.clean import clean
from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordChangeForm
from django.contrib import messages
import random


class loginForm(forms.Form):
    email=forms.CharField(widget=forms.TextInput(attrs={"class":"sign__input","placeHolder":"E-mail"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"sign__input","placeHolder":"Şifre"}))
    remember=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput()) # Başlangıç değeri False,Beni Hatırla seçeneğine tıklanırsa True oluyor

    
    def clean_email(self): # self ilgili form'a ait objeyi,referansı temsil eder.
        email=self.cleaned_data.get("email")

        if not User.objects.filter(email=email).exists():
            self.add_error("email","E-mail ile kayıtlı bir kullanıcı bulunamadı!") # form içerisindeki (ilgili değer) email'e ait olan {{ form.email.errors }} üzerinden hata mesajını yazdırılcak

        return email

#------------------------------------------------------------------------------------------------------------

class loginForm2(AuthenticationForm): 
    def __init__(self, *args,**kwargs): # AuthenticationForm'un içerisinde olan __init__ method'unu çağırdık
        super().__init__(*args, **kwargs)
        # Authentication Formu özelleştirdik
        self.fields["username"].widget=widgets.TextInput(attrs={"class":"sign__input","placeHolder":"E-mail"})
        self.fields["password"].widget=widgets.PasswordInput(attrs={"class":"sign__input","placeHolder":"Şifre"})

    def clean_username(self):
        username=self.cleaned_data.get("username")

        if username == "ilkerturan38":
            messages.add_message(self.request,messages.ERROR,'Hoşgeldin Admin')
        return username

    def confirm_login_allowed(self, user): # Hangi kullanıcıların oturum açabileceğini belirlemek için kullanılır.
        if user.username.startswith('s'): 
            self.add_error("username","Bu kullanıcı adıyla giriş yapamassınız!")

#------------------------------------------------------------------------------------------------------------

class registerForm(UserCreationForm):
    class Meta: # UserCreationForm'u içerisinde olmayan alanları,Başka model'den alıp form içerisine ekleyip sayfada gösterdik
        model=User
        fields=("email","first_name","last_name",)

    def __init__(self, *args,**kwargs): # UserCreationForm'un içerisinde olan __init__ method'unu çağırdık
        super().__init__(*args, **kwargs)
        # UserCreation Formu özelleştirdik
        self.fields["password1"].widget=widgets.PasswordInput(attrs={"class":"sign__input","placeHolder":"Parola"})
        self.fields["password2"].widget=widgets.PasswordInput(attrs={"class":"sign__input","placeHolder":"Parola Tekrar"})
        self.fields["first_name"].widget=widgets.TextInput(attrs={"class":"sign__input","placeHolder":"Ad"})
        self.fields["last_name"].widget=widgets.TextInput(attrs={"class":"sign__input","placeHolder":"Soyad"})
        self.fields["email"].widget=widgets.EmailInput(attrs={"class":"sign__input","placeHolder":"E-posta"})
        self.fields["first_name"].required=True
        self.fields["last_name"].required=True

    def clean_first_name(self):
        first_name=self.cleaned_data.get("first_name")
        onceki_karakterler =   [
                          " ",
                          "ç",
                          "ö",
                          "ğ",
                          "ü",
                          "ı",
                          "ş",
                          "Ş",
                          "Ç",
                          "Ö",
                          "Ğ",
                          "Ü",
                          "İ"
                          ]

        sonraki_karakterler =   [
                        "-",
                        "c",
                        "o",
                        "g",
                        "u",
                        "i",
                        "s",
                        "S",
                        "C",
                        "O",
                        "G",
                        "U",
                        "I"]

        for i in range(11):
            first_name=first_name.replace(onceki_karakterler[i],sonraki_karakterler[i]).lower()

        return first_name


    def clean_last_name(self):
        last_name=self.cleaned_data.get("last_name")
        onceki_karakterler =      [
                          " ",  # Türkçe Karakter Sıralamasında eğer ilk karakter Örn; Ç olduğunu varsayalım. Ç girilirse soyad'a ilk karakteri ingilizce'ye çevirmiyordu. ilk Karaktere boşluk değeri atandı.
                          "ç",
                          "ö",
                          "ğ",
                          "ü",
                          "ı",
                          "ş",
                          "Ş",
                          "Ç",
                          "Ö",
                          "Ğ",
                          "Ü",
                          "İ"
                          ]

        sonraki_karakterler =   [
                        "-",
                        "c",
                        "o",
                        "g",
                        "u",
                        "i",
                        "s",
                        "S",
                        "C",
                        "O",
                        "G",
                        "U",
                        "I"]

        for i in range(11):
            last_name=last_name.replace(onceki_karakterler[i],sonraki_karakterler[i]).lower()
        return last_name


    # Kayıt sırasında kullanıcının girdiği ad ve soyad'a göre Otomatik olarak username oluşturma İşlemi .. 
    def save(self, commit=True):
        user = super(UserCreationForm,self).save(commit=False) # UserCreationForm içerisindeki save method'u veritabanına kaydedilmeden çalıştırıp,user isimli obje ürettik.(Save methodu'nu ezdik)
        user.set_password(self.cleaned_data["password1"]) # oluşturulan obje üzerinden belirtilen alanlara,modeldeki başka alanlar atandı.
        user.username="%s_%s_%s" % (self.cleaned_data.get("first_name").lower(),self.cleaned_data.get("last_name").lower(),random.randint(11111,99999)) # %s (f string)

        if commit:
            user.save()
        return user


    def clean_email(self):
        email=self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            self.add_error("email","Bu E-mail adresiyle kayıtlı bir hesap mevcut!")

        return email

#------------------------------------------------------------------------------------------------------------

class registerFormIki(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"sign__input","placeHolder":"Kullanıcı Adı"}))
    email=forms.CharField(widget=forms.TextInput(attrs={"class":"sign__input","placeHolder":"E-mail"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"sign__input","placeHolder":"Şifre"}))
    re_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"sign__input","placeHolder":"Şifre Tekrar"}))

#------------------------------------------------------------------------------------------------------------

class passwordForm(PasswordChangeForm):
    # PasswordChangeForm (Üst) Sınıf'ta __init__ methodu içinde tanımlanan değişkenler içerisinde tutulan veriler kaybolmadan super() ile alındı,PasswordForm (Alt) sınıfı içerisine aktarıldı
    def __init__(self, *args,**kwargs): 
        super().__init__(*args, **kwargs) # 
        self.fields["old_password"].widget=widgets.PasswordInput(attrs={"class":"sign__input" })
        self.fields["new_password1"].widget=widgets.PasswordInput(attrs={"class":"sign__input"})
        self.fields["new_password2"].widget=widgets.PasswordInput(attrs={"class":"sign__input"})

    # old_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"sign__input","placeHolder":"Eski Şifre"}))
    # new_password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"sign__input","placeHolder":"Yeni Şifre"}))
    # new_password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"sign__input","placeHolder":"Yeni Şifre Tekrar"}))

#-------------------------------------------------------------------------------------------------------------

# İki tane ayrı Model içerisinden bilgiler alıncağı için İki Form oluşturulcak, Ve bu İki Form Tek bir sayfa üzerinde gösterilcek.

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=("first_name","last_name","email",)

    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget=widgets.TextInput(attrs={"class":"form-control" })
        self.fields["last_name"].widget=widgets.TextInput(attrs={"class":"form-control"})
        self.fields["email"].widget=widgets.EmailInput(attrs={"class":"form-control"})


class ProfileForm(forms.ModelForm):
    class Meta:
        model=profile
        fields=("image","location",)

    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)

        self.fields["location"].widget=widgets.TextInput(attrs={"class":"form-control"})

#-------------------------------------------------------------------------------------------------------------
