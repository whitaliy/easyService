from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
#import mptt

# Create your models here.
User = get_user_model()

class Dir(models.Model):
    name = models.CharField(verbose_name=_("Категория"), max_length=40)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'

class Buildings (models.Model):
    dir = models.ForeignKey(Dir, verbose_name=_("Категория"), on_delete=models.CASCADE, related_name="buildings")
    name = models.CharField(verbose_name=_("Корпус"), max_length=40)
    def __str__(self):
        return self.dir.name+'      '+self.name
    class Meta:
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпус'

class Сabinet (models.Model):
    #dir = models.ForeignKey(Dir, verbose_name=_("Категория"), on_delete=models.CASCADE)
    buildings = models.ForeignKey(Buildings, verbose_name=_("Корпус"), on_delete=models.CASCADE, related_name="cabinets")
    name = models.CharField(verbose_name=_("Помещение"), max_length=40)
    def __str__(self):
        return self.name+'  '+self.buildings.dir.name+'  ' +self.buildings.name

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещение'

class Type (models.Model):

    name = models.CharField(verbose_name=_("Тип актива"), max_length=40)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Тип актива'
        verbose_name_plural = 'Тип актива'

class Object (models.Model):
    dir = models.ForeignKey(Dir, verbose_name=_("Категория"), on_delete=models.CASCADE, blank=True,null=True)
    buildings = models.ForeignKey(Buildings, verbose_name=_("Корпус"), on_delete=models.CASCADE, blank=True,null=True)
    cabinet=models.ForeignKey(Сabinet, verbose_name=_("Помещение"), on_delete=models.CASCADE, blank=True,null=True)
    #parent = models.ForeignKey(self, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Родитель", related_name='child') #для дерева в админке
    type = models.ForeignKey(Type, verbose_name=_("Объект"), on_delete=models.CASCADE, max_length=40, help_text="Выберите тип актива")
    serial=models.BigIntegerField(verbose_name=_("инв. номер"), unique=True, help_text="Поле должно быть уникальным", error_messages={"unique": "Поле должно быть уникальным"})
    name=models.CharField(verbose_name=_("Название актива"), max_length=40)
    model=models.CharField(verbose_name=_("Модель актива"), max_length=40)
    ip=models.CharField(verbose_name=_("Ip адрес"), max_length=40)
    mac=models.CharField(verbose_name=_("Mac адрес"), max_length=40, help_text="Пример: 4c:4e:35:36:08:c1")
    note=models.TextField(verbose_name=_("Примечание"))
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актив'
        verbose_name_plural = 'Актив'
#     def __unicode__(self): #для дерева в админке
#         return self.name #для дерева в админке
# mptt.register(Object,) #для дерева в админке




