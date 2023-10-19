from django import forms
from django.core.exceptions import ValidationError
from .models import Docente


class BlueBackgroundTextInput(forms.TextInput):
    class Media:
        CSS = {'all': ('core/css/blue_background_text_input.css',)}


class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre de contacto", widget=BlueBackgroundTextInput, required=True)
    apellido =forms.CharField(label="Apellido de contacto", widget=forms.TextInput(attrs={'class': 'fondo_rojo'}), required=True)
    edad = forms.IntegerField(label="Edad")
    dni = forms.IntegerField(label="DNI")
    mail = forms.EmailField(label="Mail", required=True)
    mensaje =  forms.CharField(widget=forms.Textarea)

    def clean_edad(self):
        if self.cleaned_data["edad"] < 18:
            raise ValidationError("El usuario no puede tener menos de 18 años")
        
        return self.cleaned_data["edad"]

    def clean(self):
        # Este if simula una busqueda en la base de datos
        if self.cleaned_data["nombre"] == "Carlos" and self.cleaned_data["apellido"] == "Lopez":
            raise ValidationError("El usuario Carlos Lopez ya existe")
        
        # Si el usuario no existe lo damos de alta

        return self.cleaned_data
    

class AltaAlumnoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del alumn@", required=True)
    apellido =forms.CharField(label="Apellido del alumn@", required=True)
    dni = forms.IntegerField(label="DNI", required=True)
    email = forms.EmailField(label="email", required=True)
    legajo = forms.CharField(label="Legajo", required=True)


class AltaDocenteModelForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'

    def clean_cuit(self):
        cuit = self.cuit.strip() # Eliminar espacios en blanco al principio y al final

        if not cuit.isdigit():
            raise ValidationError("El CUIT debe contener solo dígitos.")

        if len(cuit) != 11:
            raise ValidationError("El CUIT debe tener 11 dígitos.")
        
        self.changed_data['cuit'] = cuit
        return self.changed_data['cuit']