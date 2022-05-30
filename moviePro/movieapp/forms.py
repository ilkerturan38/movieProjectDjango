
import re
from django import forms
from django.core.validators import MinLengthValidator,MaxLengthValidator,MaxValueValidator,MinValueValidator


class commentForm(forms.Form):
    mesaj=forms.CharField(widget=forms.Textarea(attrs={'rows': 5,'class': 'form__textarea','id':'mesaj'}))
    nameSurname=forms.CharField(min_length=8,max_length=20,widget=forms.TextInput(attrs={'class':'form__input','id':'nameSurname'}))
    email=forms.EmailField(min_length=10,max_length=40,widget=forms.EmailInput(attrs={'class':'form__input','id':'email'}))
    
    # movieID=forms.CharField(widget = forms.HiddenInput(), required = False)
    numbers=(
            ('1','1 Yıldız'),
            ('2','2 Yıldız'),
            ('3','3 Yıldız'),
            ('4','4 Yıldız'),
            ('5','5 Yıldız')
    )
    rating=forms.CharField(widget=forms.Select(choices=numbers,attrs={'class': 'form__input','id':'rating'}))


    # Doğrulamayı birden çok alan arasında (tek bir fonksiyon içerisinde) yapma işlemi
    def clean(self):
        cleaned_data=super().clean()
        nameSurname=self.cleaned_data['nameSurname']
        mesaj=self.cleaned_data['mesaj']

        if not re.search("[a-z\sA-Z]",nameSurname):
            raise forms.ValidationError("Ad-Soyad için Sadece Alfabetik değerler girebilirsiniz!")

        if len(mesaj)<8:
            raise forms.ValidationError("Mesaj gönderebilmek için en az 8 karakter girmelisin!")

        if mesaj.isdigit():
            raise forms.ValidationError("Mesaj gönderebilmek sadece Alfabetik karakter girmelisin!")


    
'''
    # Tek bir alan üzerinden Doğrulama işlemi
    
    def clean_nameSurname(self):
        nameSurname=self.cleaned_data['nameSurname']

        if not re.search("[a-z\sA-Z]",nameSurname):
            raise forms.ValidationError("Ad-Soyad için Sadece Alfabetik değerler girebilirsiniz!")

        return nameSurname

    
    def clean_mesaj(self):
        mesaj=self.cleaned_data['mesaj']

        if len(mesaj)<8:
            raise forms.ValidationError("Mesaj gönderebilmek için en az 8 karakter girmelisin!")

        if mesaj.isdigit():
            raise forms.ValidationError("Mesaj gönderebilmek sadece Alfabetik karakter girmelisin!")

        return mesaj
'''
