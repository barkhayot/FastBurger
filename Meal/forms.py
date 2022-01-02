from django import forms
from django.forms import ModelForm
from .models import Food
from Order.models import testOrder

class OrderFoodForm(ModelForm):
    class Meta:
        model   = testOrder
        fields  = ['count', 'order_t'] 