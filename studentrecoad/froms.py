from django import forms
from.models import *

class stufrom(forms.ModelForm):
    class Meta:
        model=student
        fields=['name','Email','Marks','address']