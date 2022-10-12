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

class Doctor(AbstractBaseModel):
    name = models.CharField(verbose_name='Nome', max_length=255)
    class Meta:
        verbose_name = 'Doutor'
        verbose_name_plural = 'Doutores'

    def __str__(self):
        return f'{self.name}'

class Patient(AbstractBaseModel):
    first_name = models.CharField(verbose_name='Nome', max_length=255)
    last_name = models.CharField(verbose_name = 'Sobrenome', max_length=255)
    birth_date = models.DateField(verbose_name='Data de Nascimento', null=True, blank=True)
    schooling = models.CharField(verbose_name='Escolaridade', choices=SCHOOLING_CHOICES,  max_length=255)
    handed_skill = models.CharField(verbose_name='Habilidade Manual', choices=HAND_CHOICE, max_length=255, null=True, blank=True)
    sended_by = models.ForeignKey('patient.Doctor', verbose_name='Encaminhado por', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'