from django.db import models

class UnityMeasures(models.TextChoices):
    UN = 'un', 'Unidade'
    KG = 'kg', 'Kilogramas'