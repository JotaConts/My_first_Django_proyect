from django import forms

class CreateNewList(forms.Form):
    #aqui se definen los camnpos que contendrá el formulario:
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)
