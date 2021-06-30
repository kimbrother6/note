from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Sentence(models.Model):
    EN_word = models.TextField(null=True, blank=True)
    KO_word = models.TextField(null=True, blank=True)
    memorize = models.CharField(max_length=50, null=True, blank=True)
    Class = models.CharField(max_length=30, null=True, blank=True) #class 로는 이름이 정의되지 않는다.

    def __str__(self):
        return self.EN_word