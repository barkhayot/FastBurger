from django import forms
from django.forms import ModelForm
from Order.models import testOrder

class OrderCompleteForm(ModelForm):
    class Meta:
        model = testOrder
        fields = ['status']