from django import forms
class form_comprador(forms.Form):
    nombre= forms.CharField(label='nombre',max_length=20)
    apellido=forms.CharField()
    credencial= forms.IntegerField(min_value=4)
    interno=forms.IntegerField(min_value=6)

class form_vendedor(forms.Form):
    nombre= forms.CharField(label='nombre',max_length=20)
    apellido=forms.CharField()
    modelo=forms.CharField()
    kilometros= forms.IntegerField(min_value=1)
    