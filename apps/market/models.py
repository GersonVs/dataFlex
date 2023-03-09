from django.db import models
from apps.authentication.models import User, UserAddress
from apps.market.choices import UnityMeasures

class Product(models.Model):
    name          = models.CharField(max_length=200, help_text='Nome')         
    price         = models.FloatField(default=0, help_text='Preço')
    image         = models.ImageField(null=True, blank=True, help_text='Imagem')
    unity_measure = models.CharField(max_length=3, choices=UnityMeasures.choices, default=UnityMeasures.UN, help_text='Unidade de medida')

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

class Order(models.Model): 
    date         = models.DateTimeField(auto_now_add=True)
    total_value  = models.FloatField(default=0, help_text='Total do pedido')
    user         = models.ForeignKey(User, on_delete=models.CASCADE, help_text='Usuário')
    user_address = models.ForeignKey(UserAddress, on_delete=models.CASCADE, help_text='Endereço do Usuário')

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __unicode__(self):
        return self.id
    def __str__(self):
        return self.id

class OrderItem(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.CASCADE, help_text='Produto')   
    quantity    = models.FloatField(default=0, help_text='Quantidade')
    total_value = models.FloatField(default=0, help_text='Total do item')
    order       = models.ForeignKey(Order, on_delete=models.CASCADE, help_text='Pedido')

    class Meta:
        verbose_name = "Item do pedido"
        verbose_name_plural = "Items do pedido"

    def __unicode__(self):
        return self.order.id + ' - ' + self.id 
    def __str__(self):
        return self.order.id + ' - ' + self.id 