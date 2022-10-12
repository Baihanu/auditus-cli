from django.db import models
from auditus.core.models import AbstractBaseModel


SCHOOLING_CHOICES = [
    ('EB','Ensino Básico'),
    ('EF','Ensino Fundamental'),
    ('EM','Ensino Médio'),
    ('ES','Ensino Superior'),
]


HAND_CHOICE = [
    ('Canhoto', 'Canhoto'),
    ('Destro', 'Destro'),
    ('Ambidestro', 'Ambidestro')
]


class Patient(AbstractBaseModel):
    name = models.CharField(verbose_name='Nome', max_length=255)
    birth_date = models.DateField(verbose_name='Data de Nascimento', null=True, blank=True)
    schooling = models.CharField(verbose_name='Escolaridade', choices=SCHOOLING_CHOICES,  max_length=255)
    handed_skill = models.CharField(verbose_name='Habilidade Manual', choices=HAND_CHOICE, max_length=255, null=True, blank=True)
    sended_by = models.CharField(verbose_name='Enviado por', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Pacientes'
    
    def __str__(self):
        return f'{self.name}'