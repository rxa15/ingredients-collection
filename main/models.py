from django.db import models
from django.contrib.auth.models import User

class Item(models.Model): # `Item` adalah nama model pada aplikasi `main`
    name = models.CharField(max_length=100) # variabel `name` digunakan sebagai nama bahan makanan
    category = models.CharField(max_length= 50, default = 'Uncategorized') # variabel `category` digunakan sebagai kategori bahan makanan, misalnya strawberry termasuk dalam kategori fruits
    amount = models.IntegerField() # variabel `amount` mendeskripsikan banyak suatu bahan makanan
    description = models.TextField() # variabel `description` digunakan untuk mendeskripsikan makanan apa yang dapat dibuat dari bahan makanan tersebut
    user = models.ForeignKey(User, on_delete=models.CASCADE)