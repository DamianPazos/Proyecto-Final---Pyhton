from django import forms

class nuevaCerveza(forms.Form):
    marca=forms.CharField(max_length=15,required=True)
    tipo=forms.CharField(max_length=15, required=True)
    capacidad=forms.IntegerField(required=True)
    
class nuevaGaseosa(forms.Form):
    marca=forms.CharField(max_length=15,required=True)
    tipo=forms.CharField(max_length=15,required=True)
    capacidad=forms.IntegerField(required=True)    
    light=forms.BooleanField(required=False)
    
class nuevaVino(forms.Form):
    marca=forms.CharField(max_length=15,required=True)
    tipo=forms.CharField(max_length=15, required=True)
    capacidad=forms.IntegerField(required=True)