from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_deleted   = models.BooleanField(default=False, help_text="deletado")
    phone_number = models.CharField(max_length=30, null=True, blank=True, help_text='telefone')
    photo        = models.ImageField(null=True, blank=True, help_text='Foto')

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        permissions = (
            ('lock_user'  , "Can lock user"),
            ('unlock_user', "Can unlock user"),
        )

    def __unicode__(self):
        return self.username
    def __str__(self):
        return self.username

class UserAddress(models.Model):
    street     = models.CharField(max_length=150, help_text='Rua')
    number     = models.CharField(max_length=15, help_text='Número')
    complement = models.CharField(max_length=250, help_text='Complemento')
    district   = models.CharField(max_length=100, help_text='Bairro')
    city       = models.CharField(max_length=100, help_text='Cidade')
    state      = models.CharField(max_length=50, help_text='Estado')
    zip_Code   = models.IntegerField()
    user       = models.ForeignKey(User, on_delete=models.CASCADE, help_text='Usuário')

    class Meta:
        verbose_name = "Endereço do usuário"
        verbose_name_plural = "Endereços de usuários"

    def __unicode__(self):
        return f'{self.street}, Nº {self.number} | {self.district}, {self.city} - {self.state}'
    def __str__(self):
        return f'{self.street}, Nº {self.number} | {self.district}, {self.city} - {self.state}'
