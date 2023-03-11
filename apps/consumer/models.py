from django.db import models
from django.contrib.auth.models import AbstractUser

class Client(models.Model):
    name          = models.CharField(max_length=150, help_text='nome')
    document      = models.CharField(max_length=11, help_text='cpf' )
    phone_number  = models.CharField(max_length=15, help_text='telefone')
    register_date = models.DateTimeField(auto_now_add=True, help_text='data de registro')
    is_active     = models.BooleanField(default=True, help_text='está ativo')
    is_deleted    = models.BooleanField(default=False, help_text='deletado')

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        permissions = (
            ('lock_cliente'  , "Can lock cliente"),
            ('unlock_cliente', "Can unlock cliente"),
        )

    def __unicode__(self):
        return self.id + ' - ' + self.name
    def __str__(self):
        return self.id + ' - ' + self.name

class ClientAddress(models.Model):
    street     = models.CharField(max_length=150, help_text='Rua')
    number     = models.CharField(max_length=15, help_text='Número')
    complement = models.CharField(max_length=250, help_text='Complemento')
    district   = models.CharField(max_length=100, help_text='Bairro')
    city       = models.CharField(max_length=100, help_text='Cidade')
    state      = models.CharField(max_length=50, help_text='Estado')
    zip_Code   = models.IntegerField()
    client     = models.ForeignKey(Client, on_delete=models.CASCADE, help_text='Cliente')

    class Meta:
        verbose_name = "Endereço do cliente"
        verbose_name_plural = "Endereços de clientes"

    def __unicode__(self):
        return f'{self.street}, Nº {self.number} | {self.district}, {self.city} - {self.state}'
    def __str__(self):
        return f'{self.street}, Nº {self.number} | {self.district}, {self.city} - {self.state}'
