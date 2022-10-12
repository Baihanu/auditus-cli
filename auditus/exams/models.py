from django.db import models
from auditus.core.models import AbstractBaseModel


class Reason(AbstractBaseModel):
    name = models.CharField(verbose_name = 'Motivo', max_length=255)

    class Meta:
        verbose_name = 'Motivo de Encaminhamento'
        verbose_name_plural = 'Motivos de Encaminhamentos'
    
    def __str__(self):
        return f'{self.name}'


#class Exam(AbstractBaseModel):
 #   reason = models.ManyToManyField('exams.Reason') 
