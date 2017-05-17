from django import forms
from .models import Memo

class EditForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ('title', 'detail',)