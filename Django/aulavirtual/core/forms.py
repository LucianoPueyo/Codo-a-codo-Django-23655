from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre de contacto", required=True)
    apellido =forms.CharField(label="Apellido de contacto", required=True)
    edad = forms.IntegerField(label="Edad")
    mail = forms.EmailField(label="Mail", required=True)
    mensaje =  forms.CharField(widget=forms.Textarea)