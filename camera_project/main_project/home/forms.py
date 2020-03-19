from django import forms
from.models import *


class Add_camera_Forms(forms.ModelForm):
    class Meta:
        model = Add_camera
        fields = "__all__"



class Company_register_Form(forms.ModelForm):

    password_first = forms.CharField(widget=forms.PasswordInput)
    password_second = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Company_register
        fields = "__all__"

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = '__all__'



class PersonEntryForm(forms.ModelForm):

    class Meta:
        model = Person_Entry
        fields = '__all__'
