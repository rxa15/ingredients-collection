from django.forms import ModelForm
from main.models import Item # mengimport model bernama Item yang akan digunakan untuk form

class ProductForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "category", "amount", "description"]