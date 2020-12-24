from django import forms
from stations.models import Track

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['name','singer','station']