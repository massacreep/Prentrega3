from django import forms

class IntrumentoFormulario (forms.Form):

    instrumento = forms.CharField()
    marca = forms.CharField()

