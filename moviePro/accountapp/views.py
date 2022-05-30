from django.shortcuts import redirect, render

# ----------FORM-----------------
from .forms import loginForm, loginForm2,registerForm,registerFormIki,passwordForm,UserForm,ProfileForm
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordChangeForm

# ----------MODEL-----------------
from django.contrib.auth.models import User

# -------LOGIN,AUTHENTICATE-------
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout

from django.contrib import messages # Mesaj Kütüphanesi

#------------------------------------------------------------------------------------------------------------


def login(request):
    if request.user.is_authenticated:
        return redirect("index")
    form=loginForm(request.POST or None)
    if form.is_valid():
        email=form.cleaned_data.get("email")
        password=form.cleaned_data.get("password")
        remember=form.cleaned_data.get("remember")
        username=User.objects.get(email=email).username # Form ekranında giriş yaparken email'e göre giriş yapılcak ama authenticate işlemi username göre sağlandığı için,sonradan username değerini aldık.
        user=authenticate(username=username,password=password) # alınan kullanıcı adı ve şifreye göre veritabanı içerisinde ilgili kaydın olup olmadığını kontrol eder.

        if user is not None: # Kullanıcı var ise ;
            auth_login(request,user) # login() yazınca hata veriyor yukarıda takma isim tanımladık.

            if not remember: # Beni hatırla seçeneğine tıklanmamışsa ! False ise, Session süresini azalt
                request.session.set_expiry(0) # Kullanıcı tarayıcı kapattığı anda, Oturum süresi biter,Sayfaya gittiğinde yeniden giriş yapması gerekir.
                request.session.modified=True # session değişikliğine izin ver
            return redirect("index")
            
        else :
            # messages.add_message(request,messages.ERROR,'Kullanıcı adı veya Şifre Hatalı!')
            form.add_error(None,"Kullanıcı adı veya Şifre Hatalı!!") # Form ile ilişkilendirilmiş Genel hata mesajını gösterebilmek için None değeri verdik
    context={
        "form":form,
    }
    return render(request,"account/login.html",context)

#------------------------------------------------------------------------------------------------------------

def login2(request):
    if request.user.is_authenticated: 
        return redirect("index")

    if request.method=="POST":
        form=loginForm2(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)

            if user is not None:
                auth_login(request,user)
                return redirect("index")

            else : # Hata Mesajlarını sayfada görebilmek için tekrar formu yönlendirdik,Hazır Form olduğu için mesajlar AuthenticationForm'un Class'ından otomatik gelir.
                return render(request,"account/login2.html",{"form":form}) 
                
        else:
            return render(request,"account/login2.html",{"form":form})

    else: # GET kısmı
        form=loginForm2()
        return render(request,"account/login2.html",{"form":form})

#------------------------------------------------------------------------------------------------------------

def singin(request):
    if request.method=="POST":
        form=registerForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=user.username
            password=form.cleaned_data["password1"]
            user=authenticate(request,username=username,password=password)
            auth_login(request,user)
            return redirect("index")
        else:
            return render(request,"account/sing-in.html",{"form":form})

    else: # GET kısmı
        form=registerForm()
        return render(request,"account/sing-in.html",{"form":form})

#------------------------------------------------------------------------------------------------------------

def singinIki(request):
    form=registerFormIki(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data["username"]
        email=form.cleaned_data["email"]
        password=form.cleaned_data["password"]
        re_password=form.cleaned_data["re_password"]
        newUser=User(username=username,email=email,password=password)
        newUser.is_superuser=False
        newUser.is_staff=False
        newUser.is_active=True
        newUser.save()
    else:
        messages.add_message(request,messages.ERROR,'Kayıt işlemi gerçekleştirilemedi!')
        
    context={
        "form":form
    }
    return render(request,"account/sing-in2.html",context)

#------------------------------------------------------------------------------------------------------------

@login_required(login_url="login") 
def changepassword(request):
    if request.method=="POST":
        form=passwordForm(request.user,request.POST) # request.user (o anda giriş yapan kullanıcı bilgisini tutar içinde.) 
        if form.is_valid():
            user=form.save() # Değiştirilen parola bilgisi Session içerisine eklenmesi gerekli,Yoksa kullanıcı tekrardan giriş yapması gerekir!
            update_session_auth_hash(request,user)
            messages.add_message(request,messages.SUCCESS,'Parola başarılı bir şekilde değiştirildi!')
            return redirect("change-password")
        else:
            return render(request,"account/change-password.html",{"form":form})

    form=passwordForm(request.user)
    return render(request,"account/change-password.html",{"form":form})

#------------------------------------------------------------------------------------------------------------

@login_required(login_url="login") 
def profile(request):
    return render(request,"account/profile.html")

#------------------------------------------------------------------------------------------------------------

@login_required(login_url="login") 
def profile2(request):
    if request.method == "POST":
        user_form=UserForm(request.POST,instance=request.user) # POST işlemi yapıldıktan sonra'da yeni güncel bilgiler Form üzerine aktarılcak.
        profile_form=ProfileForm(request.POST,instance=request.user.profile,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("index")
        else:
            messages.add_message(request,messages.ERROR,'Lütfen bilgilerinizi kontrol ediniz!')
    else:    
        user_form=UserForm(instance=request.user)
        profile_form=ProfileForm(instance=request.user.profile)

    return render(request,"profile2/profile2.html",{
        "user_form":user_form,
        "profile_form":profile_form
    })

#------------------------------------------------------------------------------------------------------------

@login_required(login_url="login") 
def cikis(request):
    logout(request)
    return redirect("index")

#------------------------------------------------------------------------------------------------------------
