from django import forms
from django.db.models import fields
from airiq_app.models import *


class HomeDataForm(forms.ModelForm):
    class Meta:
        model = HomeData
        fields = '__all__'
